# from rest_framework.permissions import BasePermission

# class IsAdminOrReadOnly(BasePermission):
#     """
#     Custom permission to allow only admin users to make POST requests.
#     """
#     def has_permission(self, request, view):
#         # Allow GET requests for everyone, but restrict POST to admins only
#         if request.method in ['GET', 'HEAD', 'OPTIONS']:
#             return True
#         return request.user.is_staff  # Only admins can perform other actions

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admin users to perform POST, PUT, and DELETE requests.
    Everyone can perform GET requests.
    """

    def has_permission(self, request, view):
        # Allow GET requests for everyone
        if request.method in SAFE_METHODS:  # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True

        # Only allow POST, PUT, DELETE for authenticated admin users
        return request.user.is_authenticated and request.user.is_staff
