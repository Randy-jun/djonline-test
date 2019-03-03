from rest_framework import permissions
from usermanage.models import u_token_list

class CustomerAccessPermission(permissions.BasePermission):
    message = 'You have no permission'

    def has_permission(self,request, view):
        #token = request.META['HTTP_TOKEN']
        #token = params.get('token','1')
        try:
            auth = request.META["HTTP_AUTHORIZATION"]
            user,token = auth.split(":")                                                                                                             
            ut = u_token_list.objects.get(token=token)
            if ut.user.username != user:
                return False
        except Exception as e:
            return False
        return True



