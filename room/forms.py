from django import forms
from django.forms import widgets

class roomAddForm(forms.Form):
    type = (
        ('a','正常'),
        ('b','异常'),
        ('c','停电'),
        ('d','着火')
    )
    room_name = forms.CharField(label='Username', max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    room_status=forms.CharField(
            initial='a',
            widget=widgets.Select(choices=type,attrs={'class': 'btn btn-default'})
                )