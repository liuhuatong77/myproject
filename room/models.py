from django.db import models

# Create your models here.
class Room(models.Model):
    type = (
        ('a','正常'),
        ('b','异常'),
        ('c','停电'),
        ('d','着火')
    )
    room_name = models.CharField(max_length=48,blank=True,null=True)
    room_status = models.CharField(choices=type,max_length=1,default='a')
