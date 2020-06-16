import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail

from alarmLog.models import AlarmLog
from device.forms import deviceAddForm, deviceUpdateForm
from device.models import Device
from room.models import Room
from device.python_aliyun_sdk import duanxin
# Create your views here.
from userProfile.models import UserProfile

@login_required()
def device_all(request,room_id):     #查询指定机房的设备
    room = Room.objects.get(id = room_id)
    devices = room.device_set.all()

    device_window=[]
    user_id = request.user.pk
    userprofile = UserProfile.objects.get(user_id=user_id)
    email = request.user.email
    telephone = userprofile.telephone
    for i in devices:
        if i.status == 'b':  #机器出现异常
            device_window.append("在{},{}出现异常".format(room.room_name,i.device_name))
            cause = "异常"
            method ="弹窗警告"
            log_user = userprofile
            log_device = i
            AlarmLog.objects.create(cause=cause, method=method, log_device=log_device, log_user=log_user)

        if i.status == 'c':   ##机器温度过高

            send_status=send_mail('警告', '{}{}温度过高,请快速处理'.format(room.room_name,i.device_name), '1162500174@qq.com', [email])

            ##添加预警记录
            cause = "温度过高"
            method = "邮箱通知"
            log_user = userprofile   ##值班人员
            log_device = i           ##预警设备
            AlarmLog.objects.create(cause=cause,method=method,log_device=log_device,log_user=log_user)

            if send_status:
                print('邮件发送成功')
            else:
                print('邮件发送失败')

        if i.status == 'd':   #机器损坏

            duanxin(telephone)
            ##添加预警记录
            cause = "损坏"
            method = "短信通知"
            log_user = userprofile   ##值班人员
            log_device = i           ##预警设备
            AlarmLog.objects.create(cause=cause, method=method, log_device=log_device, log_user=log_user)
    dl = json.dumps(device_window)
    return render(request, 'deviceAll.html',{'devices': devices, 'room':room,'device_window':device_window,'dl':dl})
@login_required()
def device_add(request,room_id):
    if request.method == 'POST':
        form = deviceAddForm(request.POST)
        if form.is_valid():
            device_name = form.cleaned_data['device_name']
            isactive = form.cleaned_data['isactive']
            status = form.cleaned_data['status']
            temperature = form.cleaned_data['temperature']
            Device.objects.create(device_name=device_name,isactive=isactive,
                                  status=status,temperature=temperature,deviceRoom_id=room_id)
            return redirect(reverse('device_all',kwargs={"room_id":room_id}))   #返回对应机房所以机器
        else:
            form=deviceAddForm()
            return render(request, 'deviceAdd.html',{"form":form,"message":"添加设备失败"})

    else:
        form = deviceAddForm()
        return render(request, 'deviceAdd.html',{'form':form})

@login_required()
def device_update(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    if request.method == 'POST':
        form = deviceUpdateForm(request.POST)
        if form.is_valid():
            device.device_name=form.cleaned_data['device_name']
            device.isactive = form.cleaned_data['isactive']
            device.status =  form.cleaned_data['status']
            device.temperature = form.cleaned_data['temperature']
            device.save()
            return redirect(reverse('device_all',kwargs={'room_id':device.deviceRoom.pk}))
        else:
            default = {'device_name': device.device_name, 'isactive': device.isactive,
                       'status': device.status, 'temperature': device.temperature}
            form = deviceUpdateForm(default)
            return render(request, 'deviceUpdate.html', {'form': form, 'message':"更新失败"})
    else:
        default = {'device_name':device.device_name,'isactive':device.isactive,
                   'status':device.status,'temperature':device.temperature}
        form = deviceUpdateForm(default)
        return render(request, 'deviceUpdate.html',{'form':form})
@login_required()
def device_delete(request,device_id):  #删除设备
    room_id = Device.objects.get(pk=device_id).deviceRoom.pk
    Device.objects.filter(pk=device_id).delete()
    return redirect(reverse("device_all", kwargs={"room_id":room_id}))