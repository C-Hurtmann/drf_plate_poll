from rest_framework import permissions


class IsRestauratorOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.role == 'restaurateur' or request.method in permissions.SAFE_METHODS


class IsOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user