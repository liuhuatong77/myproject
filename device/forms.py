from django import forms
from django.forms import widgets

class deviceAddForm(forms.Form):
    active = (
        ('a','关闭'),
        ('b','开启'),
    )
    type = (
        ('a','正常'),
        ('b','异常'),
        ('c','温度过高'),
        ('d','损坏')
    )
    device_name = forms.CharField(label='设备名称', max_length=48,widget=forms.TextInput(attrs={'class': 'form-control'}))
    isactive=forms.CharField(
            label="开启或关闭",
            initial='a',
            widget=widgets.Select(choices=active,attrs={'class': 'btn btn-default'})
                )
    status = forms.CharField(
        label='机器状态',
        initial='a',
        widget=widgets.Select(choices=type, attrs={'class': 'btn btn-default'})
    )
    temperature = forms.CharField(label='温度', max_length=48,widget=forms.TextInput(attrs={'class': 'form-control'}))

class deviceUpdateForm(forms.Form):
    active = (
        ('a', '关闭'),
        ('b', '开启'),
    )
    type = (
        ('a', '正常'),
        ('b', '异常'),
        ('c', '温度过高'),
        ('d', '损坏')
    )
    device_name = forms.CharField(label='设备名称', max_length=48, widget=forms.TextInput(attrs={'class': 'form-control'}))
    isactive = forms.CharField(
        label="开启或关闭",
        initial='a',
        widget=widgets.Select(choices=active, attrs={'class': 'btn btn-default'})
    )
    status = forms.CharField(
        label='机器状态',
        initial='a',
        widget=widgets.Select(choices=type, attrs={'class': 'btn btn-default'})
    )
    temperature = forms.CharField(label='温度', max_length=48, widget=forms.TextInput(attrs={'class': 'form-control'}))