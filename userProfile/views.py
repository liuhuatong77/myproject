from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from userProfile.models import UserProfile
# Create your views here.
from userProfile.forms import RegistrationForm, LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return redirect('room_all')
            else:
                return render(request, 'login.html', {'form': form, 'message':'登陆失败'})
        else:
            return render(request, 'login.html', {'form': form, 'message':'Wrong password Please Try agagin'})
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})

@login_required()
def logout(request):
    auth.logout(request)
    return redirect('/login/')

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            code = form.cleaned_data['code']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username,password=password2,email=email)
            userProfile = UserProfile.objects.create(code=code,telephone=telephone, user_id=user.id)
            return redirect('login')
        else:
            return render(request,'register.html',{'form':form,'message':"注册失败"})
    else:
        form=RegistrationForm()
        return render(request,'register.html',{'form':form})
