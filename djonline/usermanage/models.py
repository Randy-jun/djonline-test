from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class organization(models.Model):
    name = models.CharField(max_length=128,unique=True)
    remark = models.CharField(max_length=256, blank=True, default='')
    is_active = models.BooleanField(default=True)

    is_delete = models.BooleanField(default=False)
    delete_time = models.DateTimeField(auto_now_add=True)#delete_time

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "组织信息表 (organization)"


class u_token_list(models.Model):
    '''token表，记录用户token及生成时间'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=128) #token
    gen_date = models.DateTimeField() #生成时间
    
    def __str__(self):
        return self.user.username



class employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    e_type = models.IntegerField(default=1)#类型0:manager,1:employee,2:partner,3:p-empl
    e_org = models.ForeignKey(organization, on_delete=models.CASCADE)#组织
    e_remark = models.CharField(max_length=256, blank=True, default='')#备注

    is_delete = models.BooleanField(default=False)
    delete_time = models.DateTimeField(auto_now_add=True)#delete_time

    def __str__(self):
        return self.user.username    
   

    def is_manager(self):        
        return self.e_type == 0
        
class partner(models.Model):
    pass


