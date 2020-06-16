from django import forms
from django.forms import widgets

class handleAddForm(forms.Form):
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
        ('d','损坏'),
    )
    handel_method = forms.CharField(
        initial='a',
        label='通知方式',
        widget=widgets.Select(choices=notice, attrs={'class': 'btn btn-default'})
    )
    handel_cause = forms.CharField(
        initial='a',
        label='机器故障类型',
        widget=widgets.Select(choices=cause_type, attrs={'class': 'btn btn-default'})
    )