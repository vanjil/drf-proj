from rest_framework import permissions

class IsOwnerOrModerator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение доступно для всех
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешение на изменение объекта предоставляется его владельцу или модератору
        is_moderator = request.user.groups.filter(name='moderators').exists()
        is_owner = obj.user == request.user
        return is_owner or is_moderator

class IsModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='moderators').exists()
