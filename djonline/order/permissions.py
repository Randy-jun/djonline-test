from rest_framework import permissions

class CustomerAccessPermission(permissions.BasePermission):
    message = 'You have no permission to change'

    def has_permission(self,request, view):
        token = request.META['HTTP_TOKEN']
        #token = params.get('token','1')
        if token == '0':
            return True
        return False