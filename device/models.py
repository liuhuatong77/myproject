from django.db import models

# Create your models here.


class Device(models.Model):
    active = (
        ('a','关闭'),
        ('b','开启'),
    )
    type= (
        ('a','正常'),
        ('b','异常'),
        ('c','温度过高'),
        ('d','损坏')
    )
    device_name = models.CharField(max_length=48, verbose_name="机器名称", blank=True,null=True)
    isactive =models.CharField(choices=active, verbose_name="开启或关闭",max_length=1, default='a')
    status = models.CharField(choices=type, verbose_name="机器状态", max_length=1, default='a')
    temperature = models.CharField(max_length=24, verbose_name="机器温度", default="60")
    deviceRoom = models.ForeignKey('room.Room', on_delete=models.CASCADE, verbose_name="机房")

    class Meta:
        verbose_name="设备"
        verbose_name_plural=verbose_name
