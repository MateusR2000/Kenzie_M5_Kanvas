from rest_framework import permissions
from rest_framework.views import Request, View

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.method in permissions.SAFE_METHODS:
            return True
        return req.user.is_authenticated and req.user.is_superuser

class IsCourseStudent(permissions.BasePermission):
    def has_object_permission(self, req: Request, view, obj):
        return req.user in obj.students.all() or req.user.is_superuser