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
                uorgid = user.employee.e_org.id

                return JsonResponse({"isLogin": True, "loginResultString": "Success",
                 "tokenID": token, "userID": user.id, "username":user.username, "unickname":user.first_name,
                  "ulevel":user.employee.e_type,"ulevelname":ulevelname[user.employee.e_type],
                  "ustatuscode":user.is_active,"ustatusflag":ustatusflag[user.is_active],"uorg":uorg,
                  "umark":user.employee.e_remark,"uorgid":uorgid})
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
            return JsonResponse({'msg': 'Unauthorized Access'}, status=401)
        if ut.user.id:
            result = func(request, **kwargs)
            return result
        else:
            return JsonResponse({'msg': 'Unauthorized Access'}, status=401)
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
        statusflag = {True:"启用",False:"禁用"}
        d['statusflag'] = statusflag[d['statuscode']]
    except Exception as e:
        return JsonResponse({"is_success":False,"error_msg":str(e)})    
    return JsonResponse({"is_success":True,"data":d})

#@check_token
def get_organization(request):
    #获取组织                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    #token = request.META.get('Authorization',0)
    try:
        auth = request.META["HTTP_AUTHORIZATION"]
        user,token = auth.split(":")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        print(user,token)                                                                                                                           
        ut = u_token_list.objects.get(token=token)
    except Exception :
        return HttpResponse("Authentication Failed !", status=401)
    
    is_all = request.GET.get('all')
    #print('is_all:',is_all)
   
    if ut.user.id :
        if is_all == '1':
            data = serializers.serialize("json", organization.objects.filter(is_delete=False,is_active=True),ensure_ascii=False)                                                                                                       
        else:
            data = serializers.serialize("json", organization.objects.filter(is_delete=False),ensure_ascii=False)
        data = json.loads(data)
        result = []
        statusflag = {True:"启用",False:"禁用"}
        for i in data:
            d = {}
            d['id'] = i['pk']
            d['name'] = i['fields']['name']
            d['remark'] = i['fields']['remark']
            d['statuscode'] = i['fields']['is_active']
            d['statusflag'] = statusflag[d['statuscode']]
            result.append(d)
        #print(result)
        ut.gen_date = datetime.datetime.now()

    return JsonResponse({"item_num":len(data),"data":result})

def delete_organization(request):
    #失效组织
    data = json.loads(request.body)
    org_id = data['org_id']
    org = organization.objects.get(pk=org_id)
    org.is_delete = True
    org.save()
    return JsonResponse({"is_success":True},status=200)

def update_organization(request):
    #update
    data = json.loads(request.body)
    #print(data)
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
    statusflag = {True:"启用",False:"禁用"}
    d['statusflag'] = statusflag[d['statuscode']]
    return JsonResponse({"is_success":True,"data":d})


def add_employee(request):
    #接受json数据，新增职员
    if request.method != 'POST':
        return HttpResponse(status=401)

    auth = request.META["HTTP_AUTHORIZATION"]
    user,token = auth.split(":")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    #(user,token)                                                                                                                           
    ut = u_token_list.objects.get(token=token)

    
    data = json.loads(request.body)
    username = data['e_username']
    password = 'William798'
    e_org_id = data['e_org_id']
    email = ''
    first_name = data['nickname']

    if ut.user.employee.e_type == 0:
        e_type = 1
    elif ut.user.employee.e_type == 2:
        e_type = 3
    else:
        JsonResponse({'error_msg:':'permission error'},status=401)

    e_remark = data['e_remark']
    if email == '':
        email = username+'@djonline.com'
    if first_name == '':
        first_name = username
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
    auth = request.META["HTTP_AUTHORIZATION"]
    user,token = auth.split(":")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    #(user,token)                                                                                                                           
    ut = u_token_list.objects.get(token=token)

    if ut.user.employee == 0:
        data = serializers.serialize("json", employee.objects.filter(e_type=1))
    elif ut.uesr.employee == 2:
        data = serializers.serialize("json", employee.objects.filter(e_type=3))
    else:
        JsonResponse({"error_msg:":"permission error"},status=401)
    


    data = json.loads(data)
    result = []
    ulevelname = {0:"管理员",1:"职员",2:"伙伴",3:"伙伴职员"}
    statusflag = {True:"启用",False:"禁用"}

    for i in data:
        d = {}
        d['id']=i['pk']
        d['username']=User.objects.get(pk=i['fields']['user']).username
        d['e_type']=i['fields']['e_type']
        d['e_type_name']=ulevelname[d['e_type']]
        d['e_org']=organization.objects.get(pk=i['fields']['e_org']).name
        d['e_org_id']= i['fields']['e_org']
        d['e_remark']=i['fields']['e_remark']
        d['nickname']= User.objects.get(pk=i['fields']['user']).first_name
        d['statuscode']=User.objects.get(pk=i['fields']['user']).is_active
        d['statusflag']=statusflag[d['statuscode']]
        result.append(d)

    return JsonResponse({"item_num":len(data),"data":result},status=200)

def delete_employee(request):
    data = json.loads(request.body)
    #print(data)
    p_id = data['id']

    auth = request.META["HTTP_AUTHORIZATION"]
    user,token = auth.split(":") 
    ut = u_token_list.objects.get(token=token)
    if ut.user.employee.e_type == 0 and ut.user.employee.e_type == 2:       
        JsonResponse({'error_msg:':'permission error'},status=401)
    
    
    emp = employee.objects.get(pk=p_id)    
    emp.user.is_active = False
    emp.is_delete = True
    emp.user.save()
    emp.save()
    return JsonResponse({"is_success":True},status=200)

def update_employee(request):
       #update
    
    auth = request.META["HTTP_AUTHORIZATION"]
    user,token = auth.split(":")
    ut = u_token_list.objects.get(token=token)
    if ut.user.employee.e_type == 0 and ut.user.employee.e_type == 2:       
        JsonResponse({'error_msg:':'permission error'},status=401)        

    data = json.loads(request.body)
    p_id = data['id']
    emp = employee.objects.get(pk=p_id)
    if emp.e_type != 1 or 3:
        JsonResponse({'error_msg':'error type'},status=401)
    user = emp.user
    p_org_id = data['org_id']
    org = organization.objects.get(pk=p_org_id)
    emp.e_org = org
    #user.email = data['email']
    user.is_active = data['statuscode']#是否有效用户
    user.first_name = data['nickname']
    emp.e_type = data['e_type']
    emp.e_remark = data['remark']
    emp.save()
    
    ulevelname = {0:"管理员",1:"职员",2:"伙伴",3:"伙伴职员"}
    statusflag = {True:"启用",False:"禁用"}
    #处理要返回的数据
    d = {}
    d['id'] = user.id
    d['username']=user.username   
    d['nickname'] = user.first_name
    d['e_remark'] = user.employee.e_remark
    d['e_org_id']=org.id
    d['e_org']=org.name
    d['e_type']=user.employee.e_type
    d['e_type_name']=ulevelname[d['e_type']]
    d['statuscode'] = user.is_active
    d['statusflag'] = statusflag[d['statuscode']]

    return JsonResponse({"is_success":True,"data":d})

def add_partner(request):
       #接受json数据，新增职员
    if request.method != 'POST':
        return HttpResponse(status=401)
    d={}
    try:
        auth = request.META["HTTP_AUTHORIZATION"]
        c_username,token = auth.split(":")
        ut = u_token_list.objects.get(token=token) # 检查token是否过期
        ut.user.employee
        if (datetime.datetime.now().replace(tzinfo=None) - ut.gen_date.replace(tzinfo=None)).days > 1:
            return JsonResponse({"error_msg:":"token已过期请重新登陆"},status=401)
    except Exception as e:
        return JsonResponse({"error_msg:":str(e)},status=401)

    c_user = User.objects.get(username=c_username)
    if not c_user.employee.is_manager():
        return JsonResponse({"error_msg:":"非管理员无法新增伙伴"},status=401)
    if not c_user.is_active or c_user.employee.is_delete:#判断用户是激活状态
        return JsonResponse({"error_msg:":"账号已失效"},status=401)
    

    data = json.loads(request.body)
    username = data['username']
    password = 'William798'#data['password']
    p_org_id = data['org_id']
    email = ''#data['email']
    first_name = data['nickname']
    e_type = data['type']
    p_remark = data['remark']
    is_active = data['statuscode']    

    if email == '':
        email = username+'@djonline.com'
    if first_name == '':
        first_name = username

 


    try:
        user = User.objects.get(username=username,is_active=False)
        #是否有已删除的用户重名，有则启用
        if user.employee.is_delete == False:
            return JsonResponse({"error_msg":"已有同名的未激活的用户"},status=401)
        user.employee.is_delete = False
        user.is_active = is_active
        user.employee.delete_time = datetime.datetime.now()
        user.email = email
        user.set_password(password)
        user.first_name = first_name
        user.is_staff = False
        user.save()

        try:
            p_org = organization.objects.get(pk=p_org_id)
            employee = user.employee
            employee.e_org = p_org
            employee.e_type = e_type
            employee.e_remark = p_remark
            employee.save()
            result=[employee]
            data = serializers.serialize("json",result,ensure_ascii=False)
            data = json.loads(data)
        except :
            user.is_active = False
            return JsonResponse({"result":str('e')})
        

    except:
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,is_active=is_active)
        user.is_staff = False
        user.save()

        try:
            p_org = organization.objects.get(pk=p_org_id)
            from .models import employee#error:local variable employee used before assignment
            result = employee.objects.create(user=user,e_org=p_org,e_type=e_type,e_remark=p_remark)
            result=[result]
            data = serializers.serialize("json",result,ensure_ascii=False)
            data = json.loads(data)
        except Exception as e:
            user.delete()
            return JsonResponse({"result":str(e)})

    ulevelname = {0:"管理员",1:"职员",2:"伙伴",3:"伙伴职员"}
    statusflag = {True:"启用",False:"禁用"}
    
    data = data[0]
    d['id']=user.id
    d['username']=user.username    
    d['e_type']= data['fields']['e_type']
    d['e_type_name']=ulevelname[d['e_type']]
    d['e_org']=organization.objects.get(pk=data['fields']['e_org']).name
    d['e_org_id']= data['fields']['e_org']
    d['e_remark']=data['fields']['e_remark']
    d['nickname']= User.objects.get(pk=data['fields']['user']).first_name
    d['statuscode']=User.objects.get(pk=data['fields']['user']).is_active
    d['statusflag']=statusflag[d['statuscode']]
  
    return JsonResponse({"is_success":True,"data":d})



def get_partner(request):
    #获取1级伙伴,return employee id not user id!!
    auth = request.META["HTTP_AUTHORIZATION"]
    user,token = auth.split(":")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    #(user,token)                                                                                                                           
    ut = u_token_list.objects.get(token=token)

    if ut.user.employee != 0:
        JsonResponse({"error_msg":"permission error"},status=401)
    data = serializers.serialize("json", employee.objects.filter(e_type=1))
    data = serializers.serialize("json", employee.objects.filter(e_type=2))
    data = json.loads(data)
    result = []
    ulevelname = {0:"管理员",1:"职员",2:"伙伴",3:"伙伴职员"}
    statusflag = {True:"启用",False:"禁用"}

    for i in data:
        d = {}
        d['id']=i['pk']
        d['username']=User.objects.get(pk=i['fields']['user']).username
        d['e_type']=i['fields']['e_type']
        d['e_type_name']=ulevelname[d['e_type']]
        d['e_org']=organization.objects.get(pk=i['fields']['e_org']).name
        d['e_org_id']= i['fields']['e_org']
        d['e_remark']=i['fields']['e_remark']
        d['nickname']= User.objects.get(pk=i['fields']['user']).first_name
        d['statuscode']=User.objects.get(pk=i['fields']['user']).is_active
        d['statusflag']=statusflag[d['statuscode']]
        result.append(d)

    return JsonResponse({"item_num":len(data),"data":result},status=200)

def delete_partner(request):
    #删除1级伙伴
    data = json.loads(request.body)
    #print(data)
    p_id = data['partner_id']
    emp = employee.objects.get(pk=p_id)
    if emp.e_type != 2:
        JsonResponse({"error_msg":"emp is not partner"},status=401)
    emp.user.is_active = False
    emp.is_delete = True
    emp.user.save()
    emp.save()
    return JsonResponse({"is_success":True},status=200)

def update_partner(request):
       #update
    data = json.loads(request.body)
    p_id = data['id']
    emp = employee.objects.get(pk=p_id)
    if emp.e_type != 2:
        JsonResponse({'error_msg':'error type'},status=401)
    user = emp.user
    p_org_id = data['org_id']
    org = organization.objects.get(pk=p_org_id)
    emp.e_org = org
    #user.email = data['email']
    user.is_active = data['statuscode']#是否有效用户
    user.first_name = data['nickname']
    emp.e_type = data['e_type']
    emp.e_remark = data['remark']
    emp.save()
    
    ulevelname = {0:"管理员",1:"职员",2:"伙伴",3:"伙伴职员"}
    statusflag = {True:"启用",False:"禁用"}
    #处理要返回的数据
    d = {}
    d['id'] = user.id
    d['username']=user.username   
    d['nickname'] = user.first_name
    d['e_remark'] = user.employee.e_remark
    d['e_org_id']=org.id
    d['e_org']=org.name
    d['e_type']=user.employee.e_type
    d['e_type_name']=ulevelname[d['e_type']]
    d['statuscode'] = user.is_active
    d['statusflag'] = statusflag[d['statuscode']]

    return JsonResponse({"is_success":True,"data":d})



def change_first_name(request):
    if request.method != 'POST':
        return HttpResponse(status=401)
    data = json.loads(request.body)
    user_id = data['user_id']
    first_name = data['first_name']
    user = User.objects.get(pk=user_id)
    user.first_name = first_name
    user.save()
    return True

def change_password(request):
    if request.method != 'POST':
        return HttpResponse(status=401)
    token = request.META['HTTP_TOKEN']
    token_list = token_list.objects.all()#需要过滤
    if token not in token_list:
       return HttpResponse(status=401) 
    user_id = data['user_id']
    user_password = data['user_password']
    new_password = data['new_password']

    user = User.objects.get(pk=user_id)
    #authenticate(user.username,user_password)验证用户本人
    user.set_password(new_password)
    user.save()
    return True
    
