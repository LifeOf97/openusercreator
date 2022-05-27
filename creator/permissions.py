from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):
    """
    Custom object level permission to allow retrieve, update and destroy actions
    for the object instance owner and staff only users.
    """
    def has_object_permission(self, request, view, obj):
        is_owner = bool(
            request.user
            and request.user.is_authenticated
            and request.user == obj
        )

        return (is_owner or request.user.is_staff)
        