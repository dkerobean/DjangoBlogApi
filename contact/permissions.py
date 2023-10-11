from rest_framework.permissions import BasePermission


class IsAdminUserPermission(BasePermission):
    def has_permission(self, request, view):

        # Check if the user is an admin
        return request.user.is_staff
