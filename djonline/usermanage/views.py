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
                ulevelname = {0:"管理员",1:"职员",2:"伙伴",3:"伙伴职员"}
                ustatusflag = {True:"可用",False:"禁用"}

                return JsonResponse({"isLogin": True, "loginResultString": "Success",
                 "tokenID": token, "userID": user.id, "username":user.username, "unickname":user.first_name,
                  "ulevel":user.employee.e_type,"ulevelname":ulevelname[user.employee.e_type],
                  "ustatuscode":user.is_active,"ustatusflag":ustatusflag[user.is_active],"umark":user.employee.e_remark})
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

def inactivate_organization(request):
    #失效组织
    data = json.loads(request.body)
    org_id = data['org_id']
    org = organization.objects.get(pk=org_id)
    org.is_active = False
    return HttpResponse(status=200)


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
    user_id = data['user_id']
    if email == '':
        email = username+'@djonline.com'
    if first_name == '':
        first_name = username



    #权限验证
    user = User.objects.get(user__id=user_id)
    if not user.is_superuser():
        return JsonResponse({"error":"非管理员无法新增职员"},status=404)

    try:
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
        user.is_staff = True
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
    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()
    return True

def add_level1_partner(request):
       #接受json数据，新增职员
    if request.method != 'POST':
        return HttpResponse(status=404)
    data = json.loads(request.body)
    username = data['p_username']
    password = data['p_password']
    p_org_id = data['p_org_id']
    email = data['email']
    first_name = data['p_first_name']
    p_level = 1
    p_remark = data['p_remark']


    #权限验证
    user_id = data['user_id']
    user = User.objects.get(pk=user_id)
    if not user.is_staff and not user.is_superuser:
        #非职员和超级管理员无法新增1级伙伴
        return JsonResponse({"error":"非职员和管理员无法新增1级伙伴"}, status=404)

    if email == '':
        email = username+'@djonline.com'
    if first_name == '':
        first_name = username
    try:
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
        user.is_staff = False
    except Exception as e:
        return JsonResponse({"result":str(e)})
    try:
        p_org = organization.objects.get(pk=p_org_id)
        result = employee.objects.create(user=user,p_org=p_org,p_level=p_level,p_remark=p_remark)
        result=[result]
        data = serializers.serialize("json",result,ensure_ascii=False)
        data = json.loads(data)
    except Exception as e:
        user.delete()
        return JsonResponse({"result":str(e)})
    return JsonResponse({"result":data})

def add_level2_partner(request):
    #接受json数据，新增职员
    if request.method != 'POST':
        return HttpResponse(status=404)
    data = json.loads(request.body)
    username = data['p_username']
    password = data['p_password']
    p_org_id = data['p_org_id']
    email = data['email']
    first_name = data['p_first_name']
    p_level = 2
    p_remark = data['p_remark']


    #权限验证
    user_id = data['user_id']
    user = User.objects.get(pk=user_id)
    if not user.is_staff and not user.is_superuser:
        #非职员和超级管理员无法新增1级伙伴
        partner = partner.objects.get(user=user)
        if partner.level !=1:
            #非一级伙伴，无法新增二级伙伴
            return JsonResponse({"error":"非职员、管理员或1级伙伴无法新增2级伙伴"}, status=404)

    if email == '':
        email = username+'@djonline.com'
    if first_name == '':
        first_name = username
    try:
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
        user.is_staff = False
    except Exception as e:
        return JsonResponse({"result":str(e)})
    try:
        p_org = organization.objects.get(pk=p_org_id)
        result = employee.objects.create(user=user,p_org=p_org,p_level=p_level,p_remark=p_remark)
        result=[result]
        data = serializers.serialize("json",result,ensure_ascii=False)
        data = json.loads(data)
    except Exception as e:
        user.delete()
        return JsonResponse({"result":str(e)})
    return JsonResponse({"result":data})

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
    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()
    return True

def change_first_name(request):
    if request.method != 'POST':
        return HttpResponse(status=404)
    data = json.loads(request.body)
    user_id = data['user_id']
    first_name = data['first_name']
    user = User.objects.get(pk=user_id)
    user.first_name = first_name
    user.save()
    return True

def change_password(request):
    if request.method != 'POST':
        return HttpResponse(status=404)
    token = request.META['HTTP_TOKEN']
    token_list = token_list.objects.all()#需要过滤
    if token not in token_list:
       return HttpResponse(status=404) 
    user_id = data['user_id']
    user_password = data['user_password']
    new_password = data['new_password']

    user = User.objects.get(pk=user_id)
    #authenticate(user.username,user_password)验证用户本人
    user.set_password(new_password)
    user.save()
    return True
    
