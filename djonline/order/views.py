from django.shortcuts import render
from order.models import o_jieji,o_order,o_songji,o_tourist
from openpyxl import Workbook
import json,time,datetime
from tempfile import NamedTemporaryFile
from django.http import HttpResponseBadRequest,HttpResponse
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

from order.serializers import o_jiejiSerializer, o_orderSerializer, o_songjiSerializer, o_touristSerializer






# Create your views here.
def add_order(request):
    '''order = o_order.objects.get(pk=1)
    jieji = o_jieji.objects.get(o_order__pk=order.id)
    songji = o_songji.objects.get(o_order__pk=order.id)
    tourist = o_tourist.objects.get(o_order__pk=order.id)'''
    order_item = ['o_type', 'o_from', 'o_time', 'o_zhidan', 'o_tijiao', 'o_shouli', 
    'o_fukuan', 'o_shoukuan', 'o_jiesuan_type', 'o_dahui_msg']
    tourist_item = ['name', 'phone_number', 'number']
    jieji_item = ['date', 'line_num', 'fee', 'address',
    'o_from', 'o_to', 'qifei_time', 'luodi_time', 'hangzhanlou']
    songji_item = ['date', 'line_num', 'fee', 'address',
    'o_from', 'o_to', 'qifei_time', 'luodi_time', 'hangzhanlou']
    data=None

    if request.method == 'POST':        
        order_dict = {}
        tourist_dict = {}
        jieji_dict = {}
        songji_dict = {}
        mark = 0
        data = json.loads(request.body)
        print(data)
        for i in order_item:
            order_dict[i] = data['order'].get(i, None)
           
        order = o_order.objects.create(**order_dict) 

        for i in tourist_item:
            tourist_dict[i] = data['tourist'].get(i, None)
        tourist_dict['o_order'] = order
        tourist = o_tourist.objects.create(**tourist_dict)       
        
        mark = mark+1
        jieji = None
        songji = None
        if 'jieji' in data.keys() and 'songji' in data.keys():
            order.delete()
            return HttpResponseBadRequest()

        if 'jieji' in data.keys():
            try:
                for i in jieji_item:
                    jieji_dict[i] = data['jieji'].get(i, None)
                jieji_dict['o_order'] = order
                jieji = o_jieji.objects.create(**jieji_dict)
                mark = mark+1
            except Exception as e:
                order.delete()
                return HttpResponse(content=e,status=400)

        if 'songji' in data.keys():
            try:
                for i in songji_item:
                    songji_dict[i] = data['songji'].get(i, None)
                songji_dict['o_order']=order
                songji = o_songji.objects.create(**songji_dict)          
                mark = mark+1
            except Exception as e:
                order.delete()
                return HttpResponse(content=e,status=400)
        mark = 0 
    
    return render(request, 'index1.html', context={'data':data})

def index(request):
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
        if order.o_type == '2':
            air = o_jieji.objects.get(o_order__id=order.id)
        if order.o_type == '1':
            air = o_songji.objects.get(o_order__id=order.id)
        data=[order.id, order.o_type, tourist.name, tourist.number, tourist.phone_number, order.remark, air.date, air.fee,
        air.address, air.line_num, air.o_from, air.o_to, air.qifei_time, air.luodi_time, air.hangzhanlou,
        order.o_from, order.o_time, order.o_zhidan, order.o_tijiao, order.o_shouli, order.o_fukuan, order.o_shoukuan, order.o_jiesuan_type,
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
def order(request,order_id):
    if request.method == 'GET':
        order_id = order_id
        order = o_order.objects.get(pk=order_id)
        tourist = o_tourist.objects.get(o_order__id=order_id)
        
        order_serializer = o_orderSerializer(order)
        tourist_serializer = o_touristSerializer(tourist)

        if order.o_type == '2':
            jieji = o_jieji.objects.get(o_order__id=order_id)
            air_serializer = o_jiejiSerializer(jieji)

        if order.o_type == '1':
            songji = o_songji.objects.get(o_order__id=order_id)
            air_serializer = o_songjiSerializer(songji)

    return Response({'order':order_serializer.data,'tourist':tourist_serializer.data,'air':air_serializer.data})

@api_view( ['POST'])
def delete_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order_id = data['order_id']
        try:
            o_order.objects.get(pk=order_id).delete()
            result_str ='successfully deleted'+str(order_id)
        except Exception as e:
            result_str ='delete failed:'+ str(e)
    return Response({'result_str':result_str})

@api_view(['POST'])
@permission_classes((CustomerAccessPermission,))
def change_order_status(request):
    if request.method == 'POST':
        try:            
            data = json.loads(request.body)
            order_id = data['order_id']
            order = o_order.objects.get(pk=order_id)
            if data['order_status'] not in ['打回','提交','已付款','已结算','暂存']:
                raise Exception('状态无效')
            order.o_status = data['order_status']
            order.save()            
        except Exception as e:
            error_msg = str(e)
            return Response({'error_msg':error_msg}, status=400)
    return Response({'result_str':'changed succeed'},status=200)

@api_view(['POST'])
@permission_classes((IsAuthenticated,CustomerAccessPermission,))
def multi_change_order_status(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            order_ids = data['order_ids']
            orders = o_order.objects.filter(id__in=order_ids)
            if data['order_status'] not in ['打回','提交','已付款','已结算','暂存']:
                raise Exception('状态无效')
            for order in orders:
                order.o_status = data['order_status']
                order.save()
        except Exception as e:
            error_msg = str(e)
            return Response({'error_msg':error_msg}, status=400)
    return Response({'result_str':'changed succeed'},status=200)



        

    