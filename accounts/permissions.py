from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        elif request.user.is_admin:
            return True
        return False
