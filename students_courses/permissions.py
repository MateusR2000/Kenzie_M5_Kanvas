from rest_framework import permissions
from rest_framework.views import Request, View

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, req: Request, view):
        return req.user.is_authenticated and req.user.is_superuser