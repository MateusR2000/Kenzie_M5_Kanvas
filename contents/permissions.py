from rest_framework import permissions
from rest_framework.views import Request, View
from django.shortcuts import get_object_or_404
from courses.models import Course

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.method in permissions.SAFE_METHODS:
            return IsCourseStudent.has_object_permission
        return req.user.is_authenticated and req.user.is_superuser
    
# class IsCourseStudent(permissions.BasePermission):
#     def has_object_permission(self, req: Request, view, obj):
#         found_course = get_object_or_404(Course, pk=obj.course_id)
#         return req.user in found_course.students.all() or req.user.

class IsCourseStudent(permissions.BasePermission):
    def has_object_permission(self, req: Request, view, obj):
        return req.method in permissions.SAFE_METHODS and  req.user in obj.course.students.all() or req.user.is_superuser


