from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        elif request.user.is_admin:
            return True
        return False
