from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from django.core import serializers
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from acct.models import Agency_t, Line_Price_t, Ref_Price_t, Application_t, Settlement_t, Tourist_t

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser,FormParser
from rest_framework.views import APIView

from acct.serializers import Agency_tSerializer, Line_Price_tSerializer, Ref_Price_tSerializer, Application_tSerializer, Tourist_tSerializer, Settlement_tSerializer

import datetime
# Create your views here.
def generate_ID(prefix,list):
    pass


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                sessionId = ""#request.session.get('_auth_user_hash',0)
                ex =""#sessionId.get_expiry_age()
                print(sessionId,ex)
                # return HttpResponseRedirect(reverse('index'))
                return JsonResponse({"is_login": True, "login_result_string": "Success", "NickName": user.first_name, "DJName": user.last_name,"sessionId":sessionId})
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


def user_logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('index'))

def orz_list(request):
    if request.method == 'GET':
        localname = '中国国际旅行社'
        agencies = Agency_t.objects.filter(localname=localname)
        serializer = Agency_tSerializer(agencies, many=True)
        item_num = len(agencies)
        return JsonResponse({ 'result': serializer.data, 'loclname': localname, 'item_num':item_num }, safe=False)
    if request.method == 'POST':
        data = FormParser().parse(request)
        serializer = Agency_tSerializer(data=data)       
        
        if serializer.is_valid():
            item = Agency_t.objects.filter(name=serializer.validated_data['name'],localname=serializer.validated_data['localname'])
            if len(item)!=0:
                return JsonResponse({'result': serializer.data, 'error': 'name should be unique'}, status=400)
            else:
                serializer.save()
                return JsonResponse({'result': serializer.data, 's': 'sucess'}, status=201)
        return JsonResponse(serializer.errors, status=400)


def orz_detail(request, pk):
    try:
        agency = Agency_t.objects.get(pk=pk)
    except Agency_t.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Agency_tSerializer(agency)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Agency_tSerializer(agency, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': serializer.data})
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        agency.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['GET', 'POST'])
def line_list(request):
    localname = '中国国际旅行社'
    if request.method == 'GET':
        line_prices = Line_Price_t.objects.filter(localname=localname)
        item_num = len(line_prices)
        top3_ref_data = {}
        for line in line_prices:
            top3_price = Ref_Price_t.objects.filter(
                line_price_fk__id=line.id)[:3]
            top3_ref_data[line.id] = Ref_Price_tSerializer(
                top3_price, many=True).data

        ref_prices = Ref_Price_t.objects.filter(localname=localname)
        serializer = Line_Price_tSerializer(line_prices, many=True)
        serializer2 = Ref_Price_tSerializer(ref_prices, many=True)
        return Response({'result': serializer.data, 'item_num': item_num,
        'user': request.user.username, 'top3_ref_prices': top3_ref_data})

    elif request.method == 'POST':
        serializer = Line_Price_tSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def line_detail(request, pk):
    try:
        line = Line_Price_t.objects.get(pk=pk)
    except Line_Price_t.DoesNotExist:
        return Response(status=status.HTTP_404_NOTFOUND)

    if request.method == 'GET':
        serializer = Line_Price_tSerializer(line)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Line_Price_tSerializer(line, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        line.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def application_list(request):
    localname = '中国国际旅行社'
    if request.method == 'GET':
        application_list = Application_t.objects.filter(localname=localname)
        serializer = Application_tSerializer(application_list, many=True)
        return Response({'result': serializer.data})

    elif request.method == 'POST':
        serializer = Application_tSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@ensure_csrf_cookie
def tourist_list(request):
    localname = '中国国际旅行社'
    if request.method == 'GET':
        tourist_list = Tourist_t.objects.filter(localname=localname)
        serializer = Tourist_tSerializer(tourist_list, many=True)
        return Response({'result': serializer.data})

    elif request.method == 'POST':
        serializer = Tourist_tSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def post(self, request, format=None):
        serializer = Ref_Price_tSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        refP = self.get_object(pk)
        refP.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
