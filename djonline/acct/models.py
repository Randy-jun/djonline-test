from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




# 组织信息表
class Agency_t(models.Model):
    name = models.CharField(max_length=128)
    remark = models.CharField(max_length=256, blank=True, default='')
    local_agency_fk = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# 线路报价表 remark备注；detail详细报价

# User_table
class DjUser_t(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    token = models.CharField(max_length=1024, default='')
    is_logged = models.BooleanField(default=False)
    local_agency_fk = models.ForeignKey(Agency_t, on_delete=models.PROTECT,default=1)
    nick_name = models.CharField(max_length=128, default='nick name')
    e_mail = models.EmailField(default='dj@dj.com.cn')

    def __str__(self):
        return self.name+'-'+self.nick_name+ '-'+self.local_agency_fk.name


class Line_Price_t(models.Model):
    name = models.CharField(max_length=64)
    remark = models.CharField(max_length=128, blank=True)
    detail = models.TextField(max_length=2048, blank=True)
    local_agency_fk = models.ForeignKey(Agency_t,on_delete=models.PROTECT,default=1)

    def __str__(self):
        return self.name


# 参考报价表
# level挡位；kind类型，price报价，line_price_fk所属线路报价单
class Ref_Price_t(models.Model):
    kind = models.CharField(max_length=64)
    price = models.FloatField()
    line_price_fk = models.ForeignKey(
        Line_Price_t, on_delete=models.PROTECT)
    local_agency_fk = models.ForeignKey(Agency_t,on_delete=models.PROTECT,default=1)

    def __str__(self):
        return self.kind+'-'+str(self.price)+'-'+self.line_price_fk.name+'-'+self.local_agency_fk.name

# 出团申请单
# data出团日期；loca_agency_fk地接社名称；angency_fk组团社名称；line_name_fk线路名称


class Application_t(models.Model):
    date = models.DateTimeField()
    local_agency_fk = models.ForeignKey(
        Agency_t, related_name='local', on_delete=models.PROTECT)
    agency_fk = models.ForeignKey(Agency_t, on_delete=models.PROTECT)
    line_name_fk = models.ForeignKey(Line_Price_t, on_delete=models.PROTECT)
    def_price_fk = models.ForeignKey(Ref_Price_t, on_delete=models.PROTECT)
    status = models.CharField(max_length=32, default="0")

    def __str__(self):
        return self.agency_fk.name+'-'+self.line_name_fk.name+'-'+str(self.date)


class Tourist_t(models.Model):  # 游客表
    name = models.CharField(max_length=64)
    amount = models.IntegerField(default=1)  # 数量
    application_fk = models.ForeignKey(
        Application_t, on_delete=models.PROTECT)
    ref_price_fk = models.ForeignKey(
        Ref_Price_t, on_delete=models.PROTECT)  # 参考报价
    fix_price = models.FloatField(default=0)  # 修正报价
    final_price = models.FloatField(default=0)  # 最终报价
    fix_remark = models.CharField(max_length=128, blank=True)  # 修正备注
    trans_price = models.FloatField(default=0)  # 调拨报价
    trans_remark = models.CharField(max_length=128, blank=True)  # 调拨备注
    trans_agency = models.CharField(max_length=128, default='0')
    # 调拨单位
    agent_price = models.FloatField(default=0)  # 代收金额
    agent_remark = models.CharField(max_length=128, blank=True)  # 代收备注
    local_agency_fk = models.ForeignKey(Agency_t,on_delete=models.PROTECT,default=1)

    def __str__(self):
        return self.name


class Settlement_t(models.Model):  # 结算表
    price = models.FloatField()  # 结算金额
    kind = models.CharField(max_length=64)  # 类型
    rec_agency_fk = models.ForeignKey(Agency_t,
                                      related_name='rec_agency', on_delete=models.PROTECT)  # 收款方
    pay_agency_fk = models.ForeignKey(
        Agency_t, on_delete=models.PROTECT,related_name='pay_agency')  # 付款方
    application_t = models.OneToOneField(
        Application_t, on_delete=models.PROTECT)  # 所属出团申请单
    local_agency_fk = models.ForeignKey(Agency_t,on_delete=models.PROTECT,default=1)

    def __str__(self):
        return self.application_t.name+'-'+self.rec_angency_fk.name+'-'+self.pay_angecy_fk.name+'-'+self.kind+'-'+self.local_agency_fk.name
