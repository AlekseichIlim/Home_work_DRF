from rest_framework import permissions


class IsModerPermission(permissions.BasePermission):
    """Определяет, является ли пользователь модератором"""

    def has_permission(self, request, view):
        user = request.user
        return user.groups.filter(name="moderator").exists()


class IsOwnerPermission(permissions.BasePermission):
    """Определяет, является ли пользователь владельцем объекта"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
