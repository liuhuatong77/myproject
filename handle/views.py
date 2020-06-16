from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from handle.forms import handleAddForm
from handle.models import Handle
# Create your views here.
@login_required()
def handle_all(request):
    handles = Handle.objects.all()
    return render(request, 'handle_all.html',{'handles': handles})

@login_required()
def handle_delete(request, handle_id):
    Handle.objects.filter(pk=handle_id).delete()
    return redirect('handle_all')
@login_required()
def handle_add(request):
    if request.method == 'POST':
        form = handleAddForm(request.POST)
        if form.is_valid():
            handel_method = form.cleaned_data['handel_method']
            handel_cause = form.cleaned_data['handel_cause']
            Handle.objects.create(handel_cause=handel_cause,handel_method=handel_method)
            return redirect('handle_all')
        else:
            form = handleAddForm()
            return render(request, 'handle_add.html', {'form': form,"message":"添加失败"})
    else:
        form =handleAddForm()
        return render(request, 'handle_add.html',{'form':form})

@login_required()
@login_required()
def handle_update(request, handle_id):
    handle = get_object_or_404(Handle, pk=handle_id)
    if request.method == 'POST':
        form = handleAddForm(request.POST)
        if form.is_valid():
            handle.handel_method=form.cleaned_data['handel_method']
            handle.handel_cause = form.cleaned_data['handel_cause']
            handle.save()
            return redirect('handle_all')
        else:
            default = {'handel_method': handle.handel_method, 'handel_cause': handle.handel_cause,}
            form = handleAddForm(default)
            return render(request, 'handle_update.html', {'form': form, 'message':"更新失败"})
    else:
        default = {'handel_method':handle.handel_method,'handel_cause':handle.handel_cause,}
        form = handleAddForm(default)
        return render(request, 'handle_update.html',{'form':form})