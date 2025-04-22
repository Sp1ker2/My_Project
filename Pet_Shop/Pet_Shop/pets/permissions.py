from rest_framework import permissions


class IsThisUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id_id == request.user.id
