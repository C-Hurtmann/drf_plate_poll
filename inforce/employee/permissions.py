from rest_framework import permissions


class IsEmployee(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.role == 'employee':
            return True
        return False