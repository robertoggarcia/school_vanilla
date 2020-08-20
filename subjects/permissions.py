from rest_framework.permissions import BasePermission, IsAuthenticated


class SubjectPermissions(BasePermission):

    def has_permission(self, request, view): # GET, POST, DELETE, PUT, actions
        if request.user and request.user.is_authenticated:
            return True
        #if not request.user.is_staff and view.action in ['list', 'students', 'retrieve']:
        #    return True
        #if not request.user.is_staff and request.method in ['POST', 'DELETE', 'UPDATE']:
        #    return False