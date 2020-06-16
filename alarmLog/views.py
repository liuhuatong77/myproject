from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from alarmLog.models import AlarmLog
# Create your views here.
@login_required()
def alarmlog_all(request):
    alarmlogs = AlarmLog.objects.all()
    return render(request, 'alarmlog_all.html', {'alarmlogs':alarmlogs})

def alarmlog_delete(request,alarmlog_id):
    AlarmLog.objects.filter(pk=alarmlog_id).delete()
    return redirect('alarmlog_all')