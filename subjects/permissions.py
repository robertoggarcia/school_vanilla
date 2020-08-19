from rest_framework.permissions import BasePermission


class SubjectPermissions(BasePermission):

    def has_permission(self, request, view): # GET, POST, DELETE, PUT, actions
        if request.user.is_staff:
            return True
        if not request.user.is_staff and view.action in ['list', 'students', 'retrieve']:
            return True
        if not request.user.is_staff and request.method in ['POST', 'DELETE', 'UPDATE']:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        if not request.user.is_staff and obj.owner == request.user:
            return True

        return False
