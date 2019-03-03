from django.shortcuts import render
from order.models import o_jieji,o_order,o_songji,o_tourist
from openpyxl import Workbook
import json,time,datetime
from tempfile import NamedTemporaryFile
from django.http import HttpResponseBadRequest,HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .permissions import CustomerAccessPermission

from usermanage.models import u_token_list

from order.serializers import o_jiejiSerializer, o_orderSerializer, o_songjiSerializer, o_touristSerializer






# Create your views here.
def add_order(request):
    '''order = o_order.objects.get(pk=1)
    jieji = o_jieji.objects.get(o_order__pk=order.id)
    songji = o_songji.objects.get(o_order__pk=order.id)
    tourist = o_tourist.objects.get(o_order__pk=order.id)'''
    order_item = ['o_type', 'o_from_org', 'o_zhidan_time', 'o_zhidan', 'o_tijiao', 'o_shouli', 
    'o_fukuan', 'o_shoukuan', 'o_jiesuan_type', 'o_dahui_msg']
    tourist_item = ['name', 'phone_number', 'number']
    jieji_item = ['date', 'line_num', 'fee', 'address',
    'o_from', 'o_to', 'qifei_time', 'luodi_time', 'hangzhanlou']
    songji_item = ['date', 'line_num', 'fee', 'address',
    'o_from', 'o_to', 'qifei_time', 'luodi_time', 'hangzhanlou']
    data=None

    auth = request.META["HTTP_AUTHORIZATION"]
    user,token = auth.split(":")                                                                                                              
    ut = u_token_list.objects.get(token=token)

    if request.method == 'POST':        
        order_dict = {}
        tourist_dict = {}
        jieji_dict = {}
        songji_dict = {}
        result = {}
        mark = 0
        data = json.loads(request.body)
        data['o_zhidan_time'] = datetime.datetime.now()
        data['o_from_org'] = ut.user.employee.e_org.name
        data['o_zhidan'] = ut.user.first_name
        print(data)
        for i in order_item:
            order_dict[i] = data.get(i, None)
        order = o_order.objects.create(**order_dict)
        order.save()
        order_dict['order_id'] = order.id
        result.update(order_dict)   

        for i in tourist_item:
            tourist_dict[i] = data.get(i, None)
        tourist_dict['o_order'] = order
        tourist = o_tourist.objects.create(**tourist_dict)
        tourist_dict['o_order'] = order.id
        result.update(tourist_dict)       
        
        mark = mark+1
        jieji = None
        songji = None
        if 'jieji' in data.keys() and 'songji' in data.keys():
            order.delete()
            return HttpResponseBadRequest()

        if data['o_type'] == '0':          
            for i in jieji_item:
                jieji_dict[i] = data.get(i, None)
            jieji_dict['o_order'] = order
            print(jieji_dict)
            jieji = o_jieji.objects.create(**jieji_dict)
            mark = mark+1
            jieji_dict['o_order'] = order.id
            result.update(jieji_dict)
            
        if data['o_type'] == '1':
            try:
                for i in songji_item:
                    songji_dict[i] = data.get(i, None)
                songji_dict['o_order']=order
                songji = o_songji.objects.create(**songji_dict)          
                mark = mark+1
                songji_dict['o_order']=order.id
                result.update(songji_dict)
            except Exception as e:
                order.delete()
                return JsonResponse({"content":str(e)},status=401)
        mark = 0 
    
    #return render(request, 'index1.html', context={'data':data})
    return JsonResponse({"is_success":True,"data":result})
def update_order(request):
    order_item = ['o_type', 'o_from_org', 'o_zhidan_time', 'o_zhidan', 'o_tijiao', 'o_shouli', 
    'o_fukuan', 'o_shoukuan', 'o_jiesuan_type', 'o_dahui_msg']
    tourist_item = ['name', 'phone_number', 'number']
    jieji_item = ['date', 'line_num', 'fee', 'address',
    'o_from', 'o_to', 'qifei_time', 'luodi_time', 'hangzhanlou']
    songji_item = ['date', 'line_num', 'fee', 'address',
    'o_from', 'o_to', 'qifei_time', 'luodi_time', 'hangzhanlou']
    data=None

    auth = request.META["HTTP_AUTHORIZATION"]
    user,token = auth.split(":")                                                                                                              
    ut = u_token_list.objects.get(token=token)

    if request.method == 'POST':        
        order_dict = {}
        tourist_dict = {}
        jieji_dict = {}
        songji_dict = {}
        result = {}
        mark = 0
        data = json.loads(request.body)

        print(data)

        order_id = data['order_id']
        
        order = o_order.objects.get(pk=order_id)
        tourist = o_tourist.obejcts.get(o_order=order)
        if data['o_type']=='0':
            o_air = o_jiejie.objects.get(o_order=order)
        elif data['o_type']=='1':
            o_air = o_songji.objects.get(o_order=order)
        else:
            JsonResponse({"error_msg:":"error o_type"},status=401)
        for i in order_item:
            order_dict[i] = data.get(i, None)
        result.update(order_dict)  
        order = o_order.objects.update(**order_dict)
        order.save() 

        for i in tourist_item:
            tourist_dict[i] = data.get(i, None)
        tourist_dict['o_order'] = order
        tourist = o_tourist.objects.update(**tourist_dict)
        tourist_dict['o_order'] = order.id
        result.update(tourist_dict)       
        
        mark = mark+1
        jieji = None
        songji = None
        if 'jieji' in data.keys() and 'songji' in data.keys():
            order.delete()
            return HttpResponseBadRequest()

        if data['o_type'] == '0':          
            for i in jieji_item:
                jieji_dict[i] = data.get(i, None)
            jieji_dict['o_order'] = order
            print(jieji_dict)
            jieji = o_jieji.objects.update(**jieji_dict)
            mark = mark+1
            jieji_dict['o_order'] = order.id
            result.update(jieji_dict)
            
        if data['o_type'] == '1':
            try:
                for i in songji_item:
                    songji_dict[i] = data.get(i, None)
                songji_dict['o_order']=order
                songji = o_songji.objects.update(**songji_dict)          
                mark = mark+1
                songji_dict['o_order']=order.id
                result.update(songji_dict)
            except Exception as e:
                order.delete()
                return JsonResponse({"content":str(e)},status=401)
        mark = 0

    return JsonResponse({"is_success":True,"data":result})

def index(request):
    try:
        auth = request.META["HTTP_AUTHORIZATION"]
        user,token = auth.split(":")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        print(user,token)                                                                                                                           
        #ut = u_token_list.objects.get(token=token)
    except Exception as e:
        return JsonResponse({'msg': 'Unauthorized Access'}, status=401)
        
    if request.method == 'GET':
        orders = o_order.objects.all()
        orders_serializer = o_orderSerializer(orders, many=True)
        data = orders_serializer.data    
        return render(request, 'index1.html', context={'title':'order_list','data':data,'show_data':'show_data'})
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password = password)


@api_view(['GET', 'POST'])
#@permission_classes((IsAuthenticated,))
def export_excel(request):
    title = ['单据编号','单据状态','游客姓名','人数','联系电话','备注','接机日期','结算金额','送达地址',
    '航班号','起飞城市','到达城市','起飞时间','落地时间','航站楼','送单门市','送单时间','制单人','提交人','受理人',
    '付款人','收款人','结算方式','打回信息']
    
    if request.method=='GET':
        orders = o_order.objects.all()
    else:
        data = json.loads(request.body)
        order_ids = data['order_ids']
        orders = o_order.objects.filter(id__in=order_ids)
    wb = Workbook()
    ws = wb.active    
    ws.append(title)
    for order in orders:
        tourist = o_tourist.objects.get(o_order__id=order.id)
        if order.o_type == '0':
            air = o_jieji.objects.get(o_order__id=order.id)
        if order.o_type == '1':
            air = o_songji.objects.get(o_order__id=order.id)
        data=[order.id, order.o_type, tourist.name, tourist.number, tourist.phone_number, order.remark, air.date, air.fee,
        air.address, air.line_num, air.o_from, air.o_to, air.qifei_time, air.luodi_time, air.hangzhanlou,
        order.o_from_org, order.o_zhidan_time, order.o_zhidan, order.o_tijiao, order.o_shouli, order.o_fukuan, order.o_shoukuan, order.o_jiesuan_type,
        order.o_dahui_msg]
        ws.append(data)
    wb.save(r'test.xlsx')
    with NamedTemporaryFile() as tmp:
        wb.save(tmp.name)
        tmp.seek(0)
        stream = tmp.read()
    response = HttpResponse(stream,content_type='application/vnd.ms-excel')
    response['Content-Disposition']='attachment; filename ='+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+'.xlsx'
    return response

@api_view(['GET', 'POST', 'UPDATE'])
def get_order(request,order_id):
    if request.method == 'GET':
        order_id = order_id
        order = o_order.objects.get(pk=order_id)
        tourist = o_tourist.objects.get(o_order__id=order_id)
        
        order_serializer = o_orderSerializer(order)
        tourist_serializer = o_touristSerializer(tourist)

        if order.o_type == '0':
            jieji = o_jieji.objects.get(o_order__id=order_id)
            air_serializer = o_jiejiSerializer(jieji)

        if order.o_type == '1':
            songji = o_songji.objects.get(o_order__id=order_id)
            air_serializer = o_songjiSerializer(songji)

        result ={}
        result.update(order_serializer.data)
        result.update(tourist_serializer.data)
        result.update(air_serializer.data)
        result['order_id']=order.id

    return Response({"is_success":True, "data":result})

def get_orders(request):
    if request.method == 'POST':
        data = request.body
        orders = o_order.objects.all()
        results = []
        for order in orders:
            result = {}
            order_serializer = o_orderSerializer(order)
            tourist = o_tourist.objects.get(o_order=order)

            tourist_serializer = o_touristSerializer(tourist)
            if order.o_type == '0':
                jieji = o_jieji.objects.get(o_order=order)
                air_serializer = o_jiejiSerializer(jieji)

            if order.o_type == '1':
                songji = o_songji.objects.get(o_order=order)
                air_serializer = o_songjiSerializer(songji)

            result.update(order_serializer.data)
            result.update(tourist_serializer.data)
            result.update(air_serializer.data)
            result['order_id']=order.id

            results.append(result)

        return JsonResponse({"is_success":True, "data":results, "item_num":len(results)})
    return JsonResponse({"error_msg":"Bad request"},status=401)




@api_view( ['POST'])
def delete_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order_id = data['order_id']
        is_success = True
        try:
            o_order.objects.get(pk=order_id).delete()
            result_str ='successfully deleted'+str(order_id)
        except Exception as e:
            is_success = False
            result_str ='delete failed:'+ str(e)
    return Response({'is_success':is_success,'result_str':result_str})

@api_view(['POST'])
#@permission_classes((CustomerAccessPermission,))
def change_order_status(request):
    if request.method == 'POST':
        auth = request.META["HTTP_AUTHORIZATION"]
        user,token = auth.split(":")                                                                                                             
        ut = u_token_list.objects.get(token=token)
        try:            
            data = json.loads(request.body)
            order_id = data['order_id']
            order = o_order.objects.get(pk=order_id)
            if data['order_status'] not in [0,1]:#0zancun,1tijiao,2jiesuan
                raise Exception('状态无效')

            if  data['order_status'] in [1,2] and ut.user.employee.e_type not in [0,1]:
                return JsonResponse({"error_msg":"非管理员和职员无法打回，修改已付款、已结算"},status=401)
            
            order.o_status = data['order_status']
            order.save()            
        except Exception as e:
            error_msg = str(e)
            return Response({'error_msg':error_msg}, status=401)
    #return Response({'result_str':'changed succeed'},status=200)
    return JsonResponse({"is_success":True})

@api_view(['POST'])
#@permission_classes((IsAuthenticated,CustomerAccessPermission,))
def multi_change_order_status(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            order_ids = data['order_ids']
            orders = o_order.objects.filter(id__in=order_ids)
            if data['order_status'] not in [2,3]:#0zancun,1tijiao,2shouli,3jiesuan
                raise Exception('状态无效')
            for order in orders:
                order.o_status = data['order_status']
                order.save()
        except Exception as e:
            error_msg = str(e)
            return Response({'error_msg':error_msg}, status=400)
    #return Response({'result_str':'changed succeed'},status=200)
    return JsonResponse({"is_success":True,"order_ids":order_ids})



        

    