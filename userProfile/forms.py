from captcha.fields import CaptchaField
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = CaptchaField(label='验证码')

class RegistrationForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    code = forms.CharField(label="工号",max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(label='电话', max_length=13, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱",widget=forms.TextInput(attrs={'class': 'form-control'}))

