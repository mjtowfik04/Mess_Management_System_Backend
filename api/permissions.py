from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        # user login থাকতে হবে
        if not request.user or not request.user.is_authenticated:
            return False

        # read request (GET, HEAD, OPTIONS) -> সব logged user পারবে
        if request.method in SAFE_METHODS:
            return True

        # write permission -> শুধু admin
        return request.user.is_staff