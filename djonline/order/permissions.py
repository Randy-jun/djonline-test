from rest_framework import permissions

class CustomerAccessPermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self,request, view):
        token = request.META['HTTP_TOKEN']
        #token = params.get('token','1')
        if token == '0':
            return True
        return False