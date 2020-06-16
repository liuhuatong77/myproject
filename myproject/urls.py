"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from device.views import device_all, device_add, device_delete, device_update
from handle.views import handle_all, handle_add, handle_delete, handle_update
from userProfile.views import login, register, logout
from room.views import room_all,room_add
from alarmLog.views import alarmlog_all, alarmlog_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('register/', register, name='register'),
    path('room/all/', room_all, name='room_all'),  #查询所以机房
    path('room/add/', room_add, name='room_add'),   #添加机房
    path('room/<int:room_id>/devices/',device_all, name='device_all'),  #查询某个机房的所以设备
    path('room/<int:room_id>/devices/add/', device_add, name="device_add"),  #添加某个机房的机器
    path('room/<int:device_id>/update/', device_update, name='device_update'),#更新机器信息
    path('room/<int:device_id>/', device_delete, name="device_delete"), # 删除设备信息
    path('alarmlog/all/',alarmlog_all, name="alarmlog_all"),  #查询警报记录
    path('alarmlog/delete/<int:alarmlog_id>/', alarmlog_delete, name="alarmlog_delete"),  # 删除指定警报记录
    path('handle/all/', handle_all, name='handle_all'),  #查询机器故障的处理方式
    path('handle/add', handle_add, name="handle_add"),  #增加机器故障预警方式
    path('handle/delete/<int:handle_id>/', handle_delete, name='handle_delete'), #删除机器故障预警方式
    path('handle/update/<int:handle_id>/', handle_update, name="handle_update"), #更新机器故障预警方式
    path('captcha', include('captcha.urls')),
]
