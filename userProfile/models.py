from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    code = models.CharField('code',max_length=24,blank=True,null=True)
    telephone = models.CharField('Telephone', max_length=13, blank=True,null=True)
    class Meta:
        verbose_name = '用户'
        verbose_name_plural=verbose_name
    def __str__(self):
        return "{}".format(self.user.__str__())