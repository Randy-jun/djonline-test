from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
import datetime, uuid, json, time
from .models import u_token_list
# Create your views here.


def user_login(request):
    #获取用户信息，返回token
    if request.method == 'POST':
        #从post中获取username和password
        #username = request.POST.get('username')
        #password = request.POST.get('password', '')
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                token = uuid.uuid4().hex
                ut = u_token_list.objects.create(user=user,token=token,gen_date=datetime.datetime.now())
                #ut.user = user
                #ut.token = token
                #ut.gen_date = datetime.datetime.now()
                request.session['tokenID'] = token
                ut.save()

                return JsonResponse({"isLogin": True, "loginResultString": "Success", "tokenID": token, "userID": user.id, "username":user.username})
            else:
                return JsonResponse({"isLogin": False, "loginResultString": "Invalid login details supplied.",
                 "user": user.name, "password": user.password})
        else:
            return JsonResponse({"isLogin": False, 
            "loginResultString": "Invalid login details supplied.", "user": username, "password": password})
    else:
        return render(request, 'login.html', {})

def is_token_pass(request):
    token = request.META['HTTP_TOKEN']    
    ut = u_token_list.object.get(token=token)
    if ut:
        if (datetime.datetime.now - ut.gen_date).days < 1:
            return True
        else:
            return False
    else:
        return False

def index(request):
    pass