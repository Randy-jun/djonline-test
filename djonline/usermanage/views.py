from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
import datetime, uuid, json, time
from .models import u_token_list, employee, partner, organization
from django.contrib.auth.models import User
from django.core import serializers

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
    return HttpResponse("good")

def add_organization(request):
    #新增组织
    data = json.loads(request.body)
    name = data['org_name'] 
    remark = data['org_remark']
    organization.objects.create(name=name,remark=remark)
    
    return JsonResponse({"result":"add success","name":name,"remark":remark})

def get_organization(request):
    #获取组织
    data = serializers.serialize("json", organization.objects.all(),ensure_ascii=False)
    data = json.loads(data)
    return JsonResponse(data,safe=False)

def add_employee(request):
    #接受json数据，新增职员
    if request.method != 'POST':
        return HttpResponse(status=404)
    data = json.loads(request.body)
    username = data['e_username']
    password = data['e_password']
    e_org_id = data['e_org_id']
    email = data['email']
    first_name = data['e_first_name']
    e_type = data['e_type']
    e_remark = data['e_remark']
    if email == '':
        email = username+'@djonline.com'
    if first_name == '':
        first_name = username
    try:
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
       
    except Exception as e:
        return JsonResponse({"result":str(e)})
    try:
        e_org = organization.objects.get(pk=e_org_id)
        result = employee.objects.create(user=user,e_org=e_org,e_type=e_type,e_remark=e_remark)
        result=[result]
        data = serializers.serialize("json",result,ensure_ascii=False)
        data = json.loads(data)
    except Exception as e:
        user.delete()
        return JsonResponse({"result":str(e)})
    return JsonResponse({"result":data})

def get_employee(request):
    #获取职员
    data = serializers.serialize("json", employee.objects.all())
    data = json.loads(data)
    return JsonResponse(data, safe=False)

def inactive_employee(request):
    #失效职员账号
    if request.method != 'POST':
        return HttpResponse(status=404)
    data = json.loads(request.body)
    user_id = data['user_id']
    user = employee.objects.get(pk=user_id)
    user.inactive()

def get_level1_partner(request):
    #获取1级伙伴
    data = serializers.serialize("json", partner.objects.filter(p_level=1))
    data = json.loads(data)
    return JsonResponse(data)

def get_level2_partner(request):
    #获取2级伙伴
    data = serializers.serialize("json", partner.objects.filter(p_level=2))
    data = json.loads(data)
    return JsonResponse(data)

def inactive_partner(request):
    #失效伙伴账号
    if request.method != 'POST':
        return HttpResponse(status=404)
    data = json.loads(request.body)
    user_id = data['user_id']
    user = partner.objects.get(pk=user_id)
    user.inactive()


