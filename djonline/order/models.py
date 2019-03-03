from django.db import models

# Create your models here.
class o_order(models.Model):
    remark = models.CharField(max_length=128, blank=True)
    o_type = models.CharField(max_length=128)
    o_from = models.CharField(max_length=128)
    o_zhidan_time = models.DateTimeField()
    o_zhidan = models.CharField(max_length=128)
    o_tijiao = models.CharField(max_length=128,null=True)
    o_tijiao_time = models.DateTimeField(null=True)
    o_shouli = models.CharField(max_length=128,null=True)
    o_fukuan = models.CharField(max_length=128,null=True)
    o_shoukuan = models.CharField(max_length=128,null=True)
    o_shoukuan_time = models.DateTimeField(null=True)
    o_jiesuan_type = models.CharField(max_length=32,null=True)
    o_dahui_msg = models.CharField(max_length=512, null=True)
    o_status = models.IntegerField(default=0)


class o_tourist(models.Model):
    o_order = models.ForeignKey(
        o_order, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    number = models.IntegerField()

class o_jieji(models.Model):
    o_order = models.ForeignKey(
        o_order, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    line_num = models.CharField(max_length=128)
    fee = models.FloatField()
    address = models.CharField(max_length=256)
    o_from = models.CharField(max_length=128)
    o_to = models.CharField(max_length=128)
    qifei_time = models.TimeField()
    luodi_time = models.TimeField()
    hangzhanlou = models.CharField(max_length=32)

class o_songji(models.Model):
    o_order = models.ForeignKey(
        o_order, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    line_num = models.CharField(max_length=128)
    fee = models.FloatField()
    address = models.CharField(max_length=256)
    o_from = models.CharField(max_length=128)
    o_to = models.CharField(max_length=128)
    qifei_time = models.TimeField()
    luodi_time = models.TimeField()
    hangzhanlou = models.CharField(max_length=32)


