from rest_framework import permissions


class IsAdminUserOrReadonly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin #SAFE_METHODS = "GET", "HEAD", "OPTIONS

