from django.db import models

# Create your models here.
class Handle(models.Model):
    notice=(
        ('a','不通知'),
        ('b','弹窗警告'),
        ('c','邮箱通知'),
        ('d','短信通知'),
    )
    cause_type = (
        ('a','正常'),
        ('b','异常'),
        ('c','温度过高'),
        ('d','损坏')
    )
    handel_method = models.CharField(choices=notice,default='a',max_length=1, verbose_name="通知方法")
    handel_cause = models.CharField(choices=cause_type,default='a', max_length=1, verbose_name='机器故障类型')