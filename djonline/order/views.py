from django.shortcuts import render
from order.models import o_jieji,o_order,o_songji,o_tourist
from openpyxl import Workbook
import json,time
# Create your views here.
def index(request):
    '''order = o_order.objects.get(pk=1)
    jieji = o_jieji.objects.get(o_order__pk=order.id)
    songji = o_songji.objects.get(o_order__pk=order.id)
    tourist = o_tourist.objects.get(o_order__pk=order.id)'''
    order_item = ['o_type', 'o_from', 'o_time', 'o_zhidan', 'o_tijiao', 'o_shouli', 
    'o_fukuan', 'o_shoukuan', 'o_jiesuan_type', 'o_dahui_msg']
    tourist_item = ['name', 'phone_number', 'number']
    jieji_item = ['jieji_date', 'jieji_line_num', 'jieji_fee', 'jiejie_address',
    'jieji_from', 'jieji_to', 'jieji_qifei_time', 'jieji_luodi_time', 'jieji_hangzhanlou']
    songji_item = ['songji_date', 'songji_line_num', 'songji_fee', 'songjie_address',
    'songji_from', 'songji_to', 'songji_qifei_time', 'songji_luodi_time', 'songji_hangzhanlou']

    if request.method == 'POST':        
        order_dict = {}
        tourist_dict = {}
        data = json.loads(request.body)
        print(data)
        for i in order_item:
            order_dict[i] = data['order'].get(i, None)
           #print(request.POST.get(i, None))
        order = o_order.objects.create(**order_dict)
        order.save()
        for i in tourist_item:
            tourist_dict[i] = data['tourist'].get(i,None)
        tourist = o_tourist.objects.create(**tourist_dict)
        tourist.o_order=order
        tourist.save()

        


    
    title = ['单据编号','单据状态','游客姓名','人数','联系电话','备注','接机日期','结算金额','送达地址',
    '航班号','起飞城市','到达城市','起飞时间','落地时间','航站楼','送单门市','送单时间','制单人','提交人','受理人',
    '付款人','收款人','结算方式','打回信息']
    #data=[order.id, order.o_type, tourist.name, tourist.number, tourist.phone_number, order.remark, jieji.date, jieji.fee,
    #jieji.address, jieji.line_num, jieji.o_from, jieji.o_to, jieji.qifei_time, jieji.luodi_time, jieji.hangzhanlou,
    #order.o_from, order.o_time, order.o_zhidan, order.o_tijiao, order.o_shouli, order.o_fukuan, order.o_shoukuan, order.o_jiesuan_type,
    #order.o_dahui_msg]
    #show_data = dict(zip(title,data))
    '''write_excel(title,data)'''
    return render(request, 'index1.html', context={'title':title,'data':data,'show_data':'show_data'})


def write_excel(title,data):
    wb = Workbook()
    ws = wb.active    
    ws.append(title)
    ws.append(data)
    wb.save(r'test.xlsx')
