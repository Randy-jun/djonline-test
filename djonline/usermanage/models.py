from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class organization(models.Model):
    name = models.CharField(max_length=128,unique=True)
    remark = models.CharField(max_length=256, blank=True, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "组织信息表 (organization)"


class u_token_list(models.Model):
    '''token表，记录用户token及生成时间'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=128) #token
    gen_date = models.DateField() #生成时间
    
    def __str__(self):
        return self.user.username



class employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    e_type = models.IntegerField(default=1)#类型0:manager,1:employee,2:partner,3:p-empl
    e_org = models.ForeignKey(organization, on_delete=models.CASCADE)#组织
    e_remark = models.CharField(max_length=256, blank=True, default='')#备注

    def __str__(self):
        return self.user.username    
   

    def inactive(self):
        self.user.is_active = False

class partner(models.Model):
    pass


