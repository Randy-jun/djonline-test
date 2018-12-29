from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q

# Create your models here.


# 组织信息表
class Agency_t(models.Model):
    name = models.CharField(max_length=128)
    remark = models.CharField(max_length=256, blank=True, default='')
    local_agency_fk = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'local_agency_fk')
        verbose_name = "组织信息 (Agency_t)"
        verbose_name_plural = "组织信息表 (Agency_t)"


# User_table
class DjUser_t(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    token = models.CharField(max_length=1024, default='')
    is_logged = models.BooleanField(default=False)
    local_agency_fk = models.ForeignKey(
        Agency_t, on_delete=models.PROTECT, default=1)
    nick_name = models.CharField(max_length=128, default='nick name')
    e_mail = models.EmailField(default='dj@dj.com.cn')

    def __str__(self):
        return self.name+'-'+self.nick_name + '-'+self.local_agency_fk.name

    class Meta:
        unique_together = ('name', 'local_agency_fk')
        verbose_name = "用户信息 (DjUser_t)"
        verbose_name_plural = "用户信息表 (DjUser_t)"

# 线路报价表 remark备注；detail详细报价


class Line_Price_t(models.Model):
    name = models.CharField(max_length=64)
    remark = models.CharField(max_length=128, blank=True)
    detail = models.TextField(max_length=2048, blank=True)
    local_agency_fk = models.ForeignKey(
        Agency_t, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return str(self.id) + self.name

    class Meta:
        unique_together = ('name', 'local_agency_fk')
        verbose_name = "线路报价 (Line_Price_t)"
        verbose_name_plural = "线路报价表 (Line_Price_t)"


# 参考报价表
# level挡位；kind类型，price报价，line_price_fk所属线路报价单
class Ref_Price_t(models.Model):
    kind = models.CharField(max_length=64)
    price = models.FloatField()
    line_price_fk = models.ForeignKey(
        Line_Price_t, on_delete=models.PROTECT)
    local_agency_fk = models.ForeignKey(
        Agency_t, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return str(self.id)+'-'+self.kind+'-'+str(self.price)+'-'+self.line_price_fk.name+'-'+self.local_agency_fk.name

    class Meta:
        unique_together = ('kind', 'local_agency_fk', 'line_price_fk')
        verbose_name = "参考报价 (Ref_Price_t)"
        verbose_name_plural = "参考报价表 (Ref_Price_t)"

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

    def caculate_income(self, app_pk):
        app = self.objects.get(pk=app_pk)

    class Meta:
        verbose_name = "出团申请单 (Application_t)"
        verbose_name_plural = "出团申请单表 (Application_t)"


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
    local_agency_fk = models.ForeignKey(
        Agency_t, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.name

    def caculate_final_price_sum(self, app_pk):
        '''计算基础业务总金额'''
        tourists = self.objects.filter(application_fk__id=app_pk)
        base_biz_sum = 0
        for i in tourists:
            base_biz = i.final_price-i.agent_price
            base_biz_sum = base_biz_sum+base_biz
        return base_biz_sum

    def caculate_agent_price_sum(self, app_pk):
        '''计算代收金额'''
        tourists = self.objects.filter(application_fk__id=app_pk)
        agent_price_sum = 0
        for i in tourists:
            if i.trans_agency != 0:  # 没有发生调拨业务
                agent_price_sum = agent_price_sum+i.agent_price
        return agent_price_sum

    def caculate_trans_price_sum_by_trans_agency(self, app_pk, trans_pk):
        '''计算调拨总金额,app_fk：出团申请单主键,trans_fk:调拨单位主键'''
        tourists = self.objects.fiter(
            application_fk__id=app_pk, trans_agency=trans_pk)
        trans_price_sum = 0
        for i in tourists:
            trans_price_sum = trans_price_sum + i.trans_price
        return trans_price_sum

    def caculate_some_agent_price(self, app_pk, trans_pk):
        '''计算第三方代收金额'''
        tourists = self.objects.fiter(
            application_fk__id=app_pk, trans_agency=trans_pk)
        some_agent_price = 0
        for i in tourists:
            some_agent_price = some_agent_price + i.agent_price
        return some_agent_price

    def caculate_app_income(self, app_pk):
        '''计算收入'''
        base_biz_sum = self.caculate_final_price_sum(app_pk)
        agent_price_sum = self.caculate_agent_price_sum(app_pk)
        tourists = self.objects.filter(application_fk__id=app_pk)
        trans_price_sum = 0  # 总调拨金额

        for i in tourists:
            trans_price_sum = trans_price_sum + i.trans_price
        app_income = base_biz_sum + agent_price_sum - trans_price_sum

        return app_income

    class Meta:
        verbose_name = "游客信息 (Tourist_t)"
        verbose_name_plural = "游客信息表 (Tourist_t)"


class Settlement_t(models.Model):  # 结算表
    price = models.FloatField()  # 结算金额
    kind = models.CharField(max_length=64)  # 类型
    rec_agency_fk = models.ForeignKey(Agency_t,
                                      related_name='rec_agency', on_delete=models.PROTECT)  # 收款方
    pay_agency_fk = models.ForeignKey(
        Agency_t, on_delete=models.PROTECT, related_name='pay_agency')  # 付款方
    application_t = models.OneToOneField(
        Application_t, on_delete=models.PROTECT)  # 所属出团申请单
    local_agency_fk = models.ForeignKey(
        Agency_t, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.application_t.name+'-'+self.rec_angency_fk.name+'-'+self.pay_agency_fk.name+'-'+self.kind+'-'+self.local_agency_fk.name

    def get_basicbiz(self, wl_agency_pk, start_time, end_time):
        # get basic business settlement
        return self.objects.filter(Q(application_t__date__gte=start_time), Q(application_t__date_lte=end_time), kind='基础业务', pay_agency_fk=wl_agency_pk)

    def get_transbiz(self, wl_agency_pk, start_time, end_time):
        return self.objects.filter(Q(application_t__date__gte=start_time), Q(application_t__date_lte=end_time), kind='调拨业务', rec_agency_fk=wl_agency_pk)

    class Meta:
        verbose_name = "结算信息 (Settlement_t)"
        verbose_name_plural = "结算信息表 (Settlement_t)"
