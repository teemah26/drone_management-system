from rest_framework import permissions

class IsCurrentUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the current user to edit their own data.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the object.
        return obj.owner == request.user