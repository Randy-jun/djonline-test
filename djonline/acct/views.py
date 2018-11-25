from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from django.core import serializers
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from acct.models import Agency_t, Line_Price_t, Ref_Price_t, Application_t, Settlement_t, Tourist_t, DjUser_t

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.views import APIView

from acct.serializers import Agency_tSerializer, Line_Price_tSerializer, Ref_Price_tSerializer, Application_tSerializer, Tourist_tSerializer, Settlement_tSerializer

import datetime,uuid,json
# Create your views here.


def generate_ID(prefix, list):
    pass

'''
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                sessionId = ""  # request.session.get('_auth_user_hash',0)
                request.session['local_agency_fk'] = user.last_name
                # return HttpResponseRedirect(reverse('index'))
                return JsonResponse({"is_login": True, "login_result_string": "Success", "NickName": user.first_name, "DJName": user.last_name, "sessionId": sessionId})
            else:
                # return HttpResponse("your account is disabled.")
                return JsonResponse({"is_login": False, "login_result_string": "your account is disabled."})
        else:
            print("Invalid login details:{0},{1}".format(username, password))
            # return HttpResponse("Invalid login details supplied.")
            return JsonResponse({"is_login": False, "login_result_string": "Invalid login details supplied."})
    else:
        return render(request, 'login.html', {})
        # return JsonResponse({"is_login":False,"login_result_string":"No login details supplied, not POST method."})
'''

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password', '')
        user = DjUser_t.objects.get(name=username)
        if user:
            if user.password == password:
                user.token = uuid.uuid4().hex
                user.is_logged = True
                request.session['local_agency_fk'] = user.local_agency_fk.id
                request.session['tokenID'] = user.token
                user.save()
                return JsonResponse({"isLogin": True, "loginResultString": "Success", "NickName": user.nick_name, "DJName": user.local_agency_fk.name, "local_agency_fk":user.local_agency_fk.id, "tokenID": user.token, "userID":user.id})
            else:
                return JsonResponse({"isLogin": False, "loginResultString": "Invalid login details supplied.","user":user.name,"password":user.password})
        else:
            return JsonResponse({"isLogin": False, "loginResultString": "Invalid login details supplied.","user":username,"password":password})
    else:
        return render(request, 'login.html', {})

def auth_token(userID,token):
    try:
        user = DjUser_t.objects.get(id=userID)
    except:
        return False
    if user and user.token == token:
        return True
    else:
        return False

def get_token(userID):
    user = DjUser_t.objects.get(id=userID)
    if user:
        return user.token
    else:
        return False
'''def user_logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('index'))
'''

def user_logout(request,userID):
    try:
        user = DjUser_t.objects.get(pk=userID)
        user.token = ""
        user.is_logged = False
        user.save()
        return JsonResponse(status=200)
    except:
        return JsonResponse({"isLogin": False, "loginResultString": "Successfully logged out."}, status=200)

def check_token(func):
    def inner(request, **kwargs):
        user_id = request.data['user_id']
        token = request.data['token']
        if auth_token(user_id, token):
            result = func(request, **kwargs)
            return result
        else:
            return JsonResponse({'msg':'unauthorized access'}, status =200)
    return inner



@api_view(['GET', 'POST'])
def orz_list(request):
    if request.method == 'GET':
     
        agencies = Agency_t.objects.filter(local_agency_fk=1)
        serializer = Agency_tSerializer(agencies, many=True)
        item_num = len(agencies)
        return JsonResponse({'result': serializer.data, 'item_num': item_num}, safe=False)

    if request.method == 'POST' and request.data['req_method'] == 'GET' : 
        local_agency_fk = request.data['local_agency_fk']    
        agencies = Agency_t.objects.filter(local_agency_fk=local_agency_fk)
        serializer = Agency_tSerializer(agencies, many=True)
        item_num = len(agencies)
        return JsonResponse({'result': serializer.data, 'item_num': item_num, 'token':get_token(1),'status_flag':True,'stauts_string':'get data'}, safe=False, )

    if request.method == 'POST' and request.data['req_method'] == 'ADD':
        serializer = Agency_tSerializer(data=request.data)
        if serializer.is_valid():
            item = Agency_t.objects.filter(
                name=serializer.validated_data['name'], local_agency_fk=serializer.validated_data['local_agency_fk'])
            if len(item) != 0:
                return JsonResponse({'result': serializer.data, 'status_flag': False, 'status_string': 'error : name should be unique'}, status=200)
            serializer.save()
            return JsonResponse({'result': serializer.data, 'status_flag': True, 'status_string': 'Success'}, status=201)
        return JsonResponse(serializer.errors, status=200)

    if request.method == 'POST' and request.data['req_method'] == 'UPDATE':
        try:
            agency = Agency_t.objects.get(pk=request.data['pk'])
        except Agency_t.DoesNotExist:
            return JsonResponse(serializer.errors, status=200)
        serializer = Agency_tSerializer(agency, data=request.data,partial=True)
        if serializer.is_valid():
            item = Agency_t.objects.filter(
                name=serializer.validated_data['name'], local_agency_fk=serializer.validated_data['local_agency_fk'])
            if len(item)!=0 and item[0].id != agency.id:
                return JsonResponse({'result': serializer.data, 'status_flag': False, 'status_string': 'error : name should be unique'}, status=200)            
            serializer.save()
            serializer.validated_data['id'] = agency.id
            return JsonResponse({'result': serializer.validated_data, 'status_flag':True, 'status_string':'Update Success','result_count':1})
        return JsonResponse(serializer.errors, status=200)

    if request.method == 'POST' and request.data['req_method'] == 'DELETE':
        try:
            agency = Agency_t.objects.get(pk=request.data['pk'])
        except Agency_t.DoesNotExist:
            return HttpResponse(status=200)
        agency.delete()
        return JsonResponse({'status_flag': True, "status_string": "Delete Success!"}, status=200)  

          
    return JsonResponse({'status_flag':False}, status=200)


def orz_detail(request, pk):
    try:
        agency = Agency_t.objects.get(pk=pk)
    except Agency_t.DoesNotExist:
        return HttpResponse(status=200)

    if request.method == 'GET':
        serializer = Agency_tSerializer(agency)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Agency_tSerializer(agency, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': serializer.data})
        return JsonResponse(serializer.errors, status=200)

    elif request.method == 'DELETE':
        agency.delete()
        return JsonResponse({'status_flag': True, "status_string": "Delete Success!"}, status=200)


@api_view(['GET', 'POST'])
#@check_token
def line_list(request):
    
    if request.method == 'POST' and request.data['req_method'] == 'GET':
        local_agency_fk = request.data['local_agency_fk']
        line_prices = Line_Price_t.objects.filter(local_agency_fk=local_agency_fk)
        item_num = len(line_prices)
        top3_ref_data = {}
        for line in line_prices:
            top3_price = Ref_Price_t.objects.filter(
                line_price_fk__id=line.id)[:3]
            top3_ref_data[line.id] = Ref_Price_tSerializer(
                top3_price, many=True).data

        ref_prices = Ref_Price_t.objects.filter(local_agency_fk=local_agency_fk)
        serializer = Line_Price_tSerializer(line_prices, many=True)
        for i in serializer.data:
            if i['id']:
                for j in range(0, len(top3_ref_data[i['id']])):
                    i['top3_ref_data'+str(j)]=top3_ref_data[i['id']][j]['kind']+':'+str(top3_ref_data[i['id']][j]['price'])
        return Response({'result': serializer.data, 'item_num': item_num,
                         'user': request.user.username,  'status_flag': True, 'status_string': 'Success'})

    if request.method == 'POST' and request.data['req_method'] == 'ADD':
        serializer = Line_Price_tSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response({'result': serializer.data, 'status_flag': True, 'status_string': 'Success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=200)

    if request.method =='POST' and request.data['req_method'] == 'UPDATE':       
        try:
            line = Line_Price_t.objects.get(pk=request.data['pk'])
        except Line_Price_t.DoesNotExist:
            return Response({'error_message':'item does not exist'})
        serializer = Line_Price_tSerializer(line, data=request.data, partial=True)
        if serializer.is_valid():           
            serializer.save()
            serializer.validated_data['id'] = line.id
            return JsonResponse({'result': serializer.validated_data, 'status_flag':True, 'status_string':'Update Success','result_count':1})
        return JsonResponse(serializer.errors, status=200)

    if request.method == 'POST' and request.data['req_method'] == 'DELETE':
        try:
            line = Line_Price_t.objects.get(pk=request.data['pk'])
        except Agency_t.DoesNotExist:
            return HttpResponse(status=200)
        line.delete()
        return JsonResponse({'status_flag': True, "status_string": "Delete Success!"}, status=200)
        
    if request.method == 'POST' and request.data['req_method'] == 'GETONE':
        try:
            line_price = Line_Price_t.objects.get(pk=request.data['pk'])
            ref_prices = Ref_Price_t.objects.filter(
                line_price_fk__id=line_price.id)
            serializer = Line_Price_tSerializer(line_price)
            serializer2 = Ref_Price_tSerializer(ref_prices,many=True)
            result ={'line_price':serializer.data,'ref_prices':serializer2.data}
        except Line_Price_t.DoesNotExist:
            return HttpResponse(status=200)
        return JsonResponse({'result':result,'status_flag': True, "status_string": "Get one item Success!"}, status=200)
        




@api_view(['GET', 'POST'])
def application_list(request):
    local_agency_fk = request.data['local_agency_fk']
    if request.method == 'GET':
        application_list = Application_t.objects.filter(local_agency_fk=local_agency_fk)
        serializer = Application_tSerializer(application_list, many=True)
        return Response({'result': serializer.data})

    elif request.method == 'POST':
        serializer = Application_tSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_200_BAD_REQUEST)


@api_view(['GET', 'POST'])
@ensure_csrf_cookie
def tourist_list(request):
    local_agency_fk = request.data['local_agency_fk']
    if request.method == 'GET':
        tourist_list = Tourist_t.objects.filter(local_agency_fk=local_agency_fk)
        serializer = Tourist_tSerializer(tourist_list, many=True)
        return Response({'result': serializer.data})

    elif request.method == 'POST':
        serializer = Tourist_tSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_200_BAD_REQUEST)


def index(request):
    return render(request, 'index.html', context={})


def request_form_list(request):
    return render(request, 'request_form_list.html')


def request_form(request, num):
    return render(request, 'request_form.html', context={'num': num})


def new_request(request):
    return render(request, 'add_new_request.html')


def add_new_request(request):
    return render(request, 'add_new_request.html')


def calculate_acct(request, youke):
    '''核算信息计算函数
    youke是查询的游客信息表'''
    ultip_sum = 0  # 最终报价之和
    agencyp_sum = 0  # 代收金额之和
    trans_price = 0  # 非调拨的代收金额之和
    diaobo_business = {}  # 调拨业务

    for t in youke:  # tourist表

        ultip_sum = t.final_price+ultip_sum  # 累加最终报价
        agencyp_sum = t.agent_price + agencyp_sum  # 累加代收金额

        if t.trans_agency == '0':  # 通过主键查询调拨单位的名称，主键为0则是没有调拨单位的情况
            trans_agency = ''
        else:
            trans_agency = Agency_t.objects.get(
                pk=int(t.trans_agency)).name  # 通过保存的主键查询名称
        if trans_agency == '':  # 无调拨单位，总代收金额=总代收金额+当前游客代收金额
            trans_price = trans_price + t.agent_price
        else:  # 是已经在字典里的调拨单位，利用字典将相同调拨单位的调拨总额累加
            if trans_agency in diaobo_business.keys():
                diaobo_business[trans_agency] = diaobo_business[trans_agency] + \
                    t.trans_price - t.agent_price
                # 调拨业务应收【调拨单位】=调拨业务应收【调拨单位】+调拨报价-代收金额
            else:  # 新的调拨单位，调拨业务应收【调拨单位】=调拨报价-代收金额
                diaobo_business[trans_agency] = t.trans_price - t.agent_price

    amount = ultip_sum - agencyp_sum  # 应收金额=最终报价总额-代收金额总和

    # 返回应收金额，代收金额，调拨金额
    result = {'amount': amount, 'trans_price': trans_price,
              'diaobo_business': diaobo_business}

    return JsonResponse(result)


class Ref_PriceList(APIView):
    def get(self, request, format=None):
        refP = Ref_Price_t.objects.all()
        serializer = Ref_Price_tSerializer(refP, many=True)
        return Response({'result': serializer.data})

    def get_by_kind(self, kind, local_agency_fk):
        refP = Ref_Price_t.objects.filter(kind=kind,local_agency_fk__id=local_agency_fk)
        if len(refP) > 0:
            return True
        else:
            return False


    
    def post(self, request, format=None):
        print(type(request.data['data_to_add']),request.data['data_to_add'])
        add_data = request.data['data_to_add']
        print(type(add_data), add_data)
        for i in add_data:
            print(type(i), i)
            #print(i.values(), i.keys())
        if request.data['req_method'] == 'ADD':
            serializer = Ref_Price_tSerializer(data=add_data, many=True)
           
            added_num = 0
            status = []
            for data in add_data:
                serializer = Ref_Price_tSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    status.append(serializer.data['kind']+' added successfully')
                    added_num = added_num+1
                else:
                    status.append('add '+serializer.data['kind'] +'failed, error message: '+str(serializer.errors))
            return Response({'added_num':added_num,'failed_num':len(request.data['data_to_add'])-added_num,'status':status})

        if request.data['req_method'] == 'GET':#get refprice by line_price_pk and local_agency_fk
            try:
                refP = Ref_Price_t.objects.filter(local_agency_fk=request.data['local_agency_fk']).filter(line_price_fk__id=request.data['line_price_fk'])
            except KeyError:
                return Response({'status_flag':False,'status_string':'key error'}, status=200)
            serializer = Ref_Price_tSerializer(refP, many=True)
            return Response({'result': serializer.data, 'item_num':len(refP),'status_flag':True, 'status_string':'Successfully get {0} ref_price item'.format(len(refP))})

        if request.data['req_method'] == 'DELETE':
            try:
                refP = Ref_Price_t.objects.get(pk=request.data['pk'])
            except Ref_Price_t.DoesNotExist:
                return JsonResponse({'result': '', 'status_flag':False, 'status_string':'Item did not exist','result_count':0})            
            refP.delete()
            return Response({'status_flag':True,'status_string':'Successfully deleted !'}, status=200)

        if request.data['req_method'] == 'UPDATE':
            try:
                refP = Ref_Price_t.objects.get(pk=request.data['pk'])
            except Ref_Price_t.DoesNotExist:
                return JsonResponse({'result': '', 'status_flag':False, 'status_string':'Item did not exist','result_count':0})
            serializer = Ref_Price_tSerializer(refP, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'result': serializer.validated_data, 'status_flag':True, 'status_string':'Update Success','result_count':1})
        return JsonResponse(serializer.errors, status=200)
            


class Ref_PriceDetail(APIView):
    def get_object(self, pk):
        try:
            return Ref_Price_t.objects.get(pk=pk)
        except Ref_Price_t.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        refP = self.get_object(pk)
        serializer = Ref_Price_tSerializer(refP)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        refP = self.get_object(pk)
        serializer = Ref_Price_tSerializer(refP, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Reponse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_200_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        refP = self.get_object(pk)
        refP.delete()
        return Response(status=status.HTTP_200_NO_CONTENT)
