from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class organization(models.Model):
    name = models.CharField(max_length=128)
    remark = models.CharField(max_length=256, blank=True, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def inactive(self):
        self.is_active = False

    class Meta:
        verbose_name_plural = "组织信息表 (organization)"


class u_token_list(models.Model):
    '''token表，记录用户token及生成时间'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=128) #token
    gen_date = models.DateField() #生成时间
    
    def __str__(self):
        return self.user.name



class employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    e_type = models.IntegerField(default=1)#类型
    e_org = models.ForeignKey(organization, on_delete=models.CASCADE)#组织
    e_remark = models.CharField(max_length=256, blank=True, default='')#备注

    def __str__(self):
        return self.user.username    
   

    def inactive(self):
        self.user.is_active = False


    class Meta:
        verbose_name_plural = "职员"

class partner(models.Model):
    user = models.OneToOneField(User, verbose_name=("伙伴"), on_delete=models.CASCADE)
    p_level = models.IntegerField(default=1)#级别
    p_org = models.ForeignKey(organization, on_delete=models.CASCADE)#组织
    p_remark = models.CharField(max_length=256, blank=True, default='')#备注 

    def __str__(self):
        return self.user.username


    def inactive(self):
        self.user.is_active = False


    class Meta:
        verbose_name_plural = "伙伴"

