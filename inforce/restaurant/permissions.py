from rest_framework import permissions


class IsRestauratorOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.role == 'restaurateur' or request.method in permissions.SAFE_METHODS:
            return True
        return False