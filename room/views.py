from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from room.forms import roomAddForm
from room.models import Room
# Create your views here.
@login_required()
def room_all(request):
    rooms = Room.objects.all()
    return render(request,'machineRoom.html',{'rooms':rooms})
@login_required()
def room_add(request):
    if request.method == 'POST':
        form = roomAddForm(request.POST)
        if form.is_valid():
            room_name = form.cleaned_data['room_name']
            room_status = form.cleaned_data['room_status']
            room = Room.objects.create(room_name=room_name,room_status=room_status)
            return redirect('room_all')
        else:
            form = roomAddForm()
            return render(request, 'roomAdd.html',{'form':form, 'message':'添加机房失败'})
    else:
        form = roomAddForm()
        return render(request, 'roomAdd.html', {'form': form})