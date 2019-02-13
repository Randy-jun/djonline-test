from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class u_token_list(models.Model):
    '''token表，记录用户token及生成时间'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=128) #token
    gen_date = models.DateField() #生成时间

class employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    e_type = models.IntegerField()
    e_org = models.CharField(max_length=128)
