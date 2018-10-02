from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from acct.models import Agency_t
import datetime
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                #return HttpResponseRedirect(reverse('index'))
                return JsonResponse({"is_login":True,"login_result_string":"Success","NickName":user.first_name,"DJName":user.last_name})
            else:
                #return HttpResponse("your account is disabled.")
                return JsonResponse({"is_login":False,"login_result_string":"your account is disabled."})
        else:
            print("Invalid login details:{0},{1}".format(username,password))
            #return HttpResponse("Invalid login details supplied.")
            return JsonResponse({"is_login":False,"login_result_string":"Invalid login details supplied."})
    else:
        return render(request,'login.html',{})
        #return JsonResponse({"is_login":False,"login_result_string":"No login details supplied, not POST method."})

@login_required
def user_logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('index'))

@login_required
def get_orz(request):
    if request.method == 'GET':
        agencies = Agency_t.objects.all()
        return JsonResponse({'agency':agencies})

@login_required
def add_orz(request):
    if request.method == 'POST':
        org_name = request.POST.get('org_name')
        org_remark = request.POST.get('remark')

        if org_name:
            agency = Agency_t(name=org_name,remark=org_remark)
            agency.save()
            return JsonResponse({"add_orz_result":"Success"})

        else:
            return JsonResponse({"add_orz_result":"Organization name should not be null or '' "})

    else:
        return JsonResponse({"add_orz_result":"not post method"})


def add_route(request):
    pass

def index(request):
    return render(request,'index.html',context={})

@login_required
def request_form_list(request):
    return render(request,'request_form_list.html')

def request_form(request,num):
    return render(request,'request_form.html',context={'num':num})

def new_request(request):
    return render(request,'add_new_request.html')

def add_new_request(request):
    return render(request,'add_new_request.html')

def return_json(request):
    testdata=[
        {
          "aid":110,
          "title":"iOS程序员的月薪已降到12K但是13k还招不到html5移动app开发者!",
        },
        {
          "aid":111,
          "title":"锤子代工厂倒闭 罗永浩:已尽力了!",
        },
        {
          "aid":112,
          "title":"ionic模板源码下载市场正式上线了",
        },
        {
          "aid":113,
          "title":"我为什么创建Ionic中文网",
        },
        {
          "aid":114,
          "title":"angularjs ionic中图表和报表插件 Chart.js的使用",
        },
        {
          "aid":115,
          "title":"angulard sagefgfdsad Chart.js的使用!",
        },
        {
          "aid":116,
          "title":"djonline first submit",
        },
    ]
    # testdata={'teststr':'This is a string','testint':2018,'testdate':datetime.datetime.now(),'testfloat':12.8,'testinner':{'a':'a','b':'b'}}
    return JsonResponse({"result":testdata})

def get_json(request):
    # print(request)
    getdata = request.POST
    if request.POST['id'] == "156":
        return JsonResponse({'result':'OK'})
    else:
        return JsonResponse({'result':'No data'})


def calculate_acct(request):
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
            trans_agency = agency_t.objects.get(
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
