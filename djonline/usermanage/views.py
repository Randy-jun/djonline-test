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
                uorg = user.employee.e_org.name

                return JsonResponse({"isLogin": True, "loginResultString": "Success",
                 "tokenID": token, "userID": user.id, "username":user.username, "unickname":user.first_name,
                  "ulevel":user.employee.e_type,"ulevelname":ulevelname[user.employee.e_type],
                  "ustatuscode":user.is_active,"ustatusflag":ustatusflag[user.is_active],"uorg":uorg,
                  "umark":user.employee.e_remark})
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



def check_token(func):
    def inner(request, **kwargs):
        try:
            auth = request.META["HTTP_AUTHORIZATION"]
            user,token = auth.split(":")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            print(user,token)                                                                                                                           
            ut = u_token_list.objects.get(token=token)
        except Exception as e:
            return JsonResponse({'msg': 'Unauthorized Access'}, status=404)
        if ut.user.id:
            result = func(request, **kwargs)
            return result
        else:
            return JsonResponse({'msg': 'Unauthorized Access'}, status=404)
    return inner

def add_organization(request):
    #新增组织 
    try: 
        data = json.loads(request.body)
        name = data['org_name']
        remark = data['org_remark']
        is_active = data['org_is_active']
        try:
            org =  organization.objects.get(name=name,is_delete=True)
            org.remark = remark
            org.is_acitve = is_active
        except:
            org = organization.objects.create(name=name,remark=remark,is_active=is_active)
        
        org.save()
        d = {}
        d['id'] = org.id
        d['name'] = org.name
        d['remark'] = org.remark
        d['statuscode'] = org.is_active
        statusflag = {True:"正常",False:"禁用"}
        d['statusflag'] = statusflag[d['statuscode']]
    except Exception as e:
        return JsonResponse({"is_success":False,"error_msg":str(e)})    
    return JsonResponse({"is_success":True,"data":d})

@check_token
def get_organization(request):
    #获取组织                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    #token = request.META.get('Authorization',0)
    try:
        auth = request.META["HTTP_AUTHORIZATION"]
        user,token = auth.split(":")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        print(user,token)                                                                                                                           
        ut = u_token_list.objects.get(token=token)
    except Exception as e:
        return HttpResponse("Authentication Failed !", status=404)

    if ut.user.id :                                                                                                         
        data = serializers.serialize("json", organization.objects.filter(is_delete=False),ensure_ascii=False)
        data = json.loads(data)
        result = []
        statusflag = {True:"正常",False:"禁用"}
        for i in data:
            d = {}
            d['id'] = i['pk']
            d['name'] = i['fields']['name']
            d['remark'] = i['fields']['remark']
            d['statuscode'] = i['fields']['is_active']
            d['statusflag'] = statusflag[d['statuscode']]
            result.append(d)
        print(result)

    return JsonResponse({"item_num":len(data),"data":result})

def delete_organization(request):
    #失效组织
    data = json.loads(request.body)
    org_id = data['org_id']
    org = organization.objects.get(pk=org_id)
    org.is_delete = True
    org.delete_time = datetime.datetime.now()
    org.save()
    return JsonResponse({"is_success":True},status=200)

def update_organization(request):
    #update
    data = json.loads(request.body)
    org_id = data['org_id']
    org = organization.objects.get(id=org_id)
    org.name = data['org_name']
    org.remark = data['org_remark']
    org.is_active = data['org_is_active']
    org.save()
    d = {}
    d['id'] = org.id
    d['name'] = org.name
    d['remark'] = org.remark
    d['statuscode'] = org.is_active
    statusflag = {True:"正常",False:"禁用"}
    d['statusflag'] = statusflag[d['statuscode']]
    return JsonResponse({"is_success":True,"data":d})


def add_employee(request):
    #接受json数据，新增职员
    if request.method != 'POST':
        return HttpResponse(status=404)

    auth = request.META["HTTP_AUTHORIZATION"]
    user,token = auth.split(":")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    print(user,token)                                                                                                                           
    ut = u_token_list.objects.get(token=token)

    
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
    user = User.objects.get(id=user_id)
    if not user.employee.is_manager():
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

def add_partner(request):
       #接受json数据，新增职员
    if request.method != 'POST':
        return HttpResponse(status=404)
    try:
        auth = request.META["HTTP_AUTHORIZATION"]
        c_username,token = auth.split(":")
        ut = u_token_list.objects.get(token=token) # 检查token是否过期
        ut.user.employee
        if (datetime.datetime.now().replace(tzinfo=None) - ut.gen_date.replace(tzinfo=None)).days > 1:
            return JsonResponse({"error_msg:":"token已过期请重新登陆"},status=404)
    except Exception as e:
        return JsonResponse({"error_msg:":str(e)},status=404)

    c_user = User.objects.get(username=c_username)
    if not c_user.employee.is_manager():
        return JsonResponse({"error_msg:":"非管理员无法新增伙伴"},status=404)
    if not c_user.is_active or c_user.employee.is_delete:#判断用户是激活状态
        return JsonResponse({"error_msg:":"账号已失效"},status=404)
    

    data = json.loads(request.body)
    username = data['p_username']
    password = data['p_password']
    p_org_id = data['p_org_id']
    email = data['email']
    first_name = data['p_first_name']
    e_type = 3
    p_remark = data['p_remark']    

    if email == '':
        email = username+'@djonline.com'
    if first_name == '':
        first_name = username
    try:
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
        user.is_staff = False
        user.save()
    except Exception as e:
        return JsonResponse({"result":str(e)})
    try:
        p_org = organization.objects.get(pk=p_org_id)
        result = employee.objects.create(user=user,e_org=p_org,e_type=e_type,e_remark=p_remark)
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

def get_partner(request):
    #获取1级伙伴
    data = serializers.serialize("json", employee.objects.filter(e_type=3))
    data = json.loads(data)
    result = []
    ulevelname = {0:"管理员",1:"职员",2:"伙伴",3:"伙伴职员"}

    for i in data:
        d = {}
        d['id']=i['pk']
        d['username']=User.objects.get(pk=i['fields']['user']).username
        d['e_type']=i['fields']['e_type']
        d['e_type_name']=ulevelname[d['e_type']]
        d['e_org']=organization.objects.get(pk=i['fields']['e_org']).name
        d['e_remark']=i['fields']['e_remark']
        result.append(d)

    return JsonResponse({"item_num":len(data),"result":result},status=200)

def get_level2_partner(request):
    #获取2级伙伴
    data = serializers.serialize("json", partner.objects.filter(e_type=4))
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
    
