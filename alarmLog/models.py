import django.utils.timezone as timezone

from django.db import models

# Create your models here.
class AlarmLog(models.Model):
    cause = models.CharField(max_length=128,blank=True,null=True)
    method = models.CharField( max_length=128,blank=True,null=True)
    add_date = models.DateTimeField(default = timezone.now)
    log_user = models.ForeignKey("userProfile.UserProfile",on_delete=models.CASCADE, verbose_name="管理员")
    log_device = models.ForeignKey("device.Device", on_delete=models.CASCADE, verbose_name="设备")