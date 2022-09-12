from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Custom object level permission to allow retrieve, update and destroy actions
    for the object instance owner and staff only users.
    """
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and request.user.is_authenticated
            and request.user == obj
        )
