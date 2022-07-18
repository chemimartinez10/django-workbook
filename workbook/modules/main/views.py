from turtle import title
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from modules.main.models import Item, ListTask

from .forms import FormList


@login_required
def index(request):
    listas = ListTask.objects.filter(user=request.user).order_by('-id')
    last_task = Item.objects.filter(list_task__user=request.user).last()
    if request.method == 'POST':
        form = FormList(data=request.POST)
        if form.is_valid():
            form.save()
            last_list = ListTask.objects.last()
            return render(request, 'main/tasks.html', {'list_data': last_list})
        else:
            print(form.errors)
    else:
        form = FormList(initial={"user": request.user})
    return render(request, 'main/index.html', {'form_list': form, 'listas': listas, 'last_task': last_task})


@login_required
def lists(request):
    listas = ListTask.objects.filter(user=request.user).order_by('-id')
    last_task = Item.objects.filter(list_task__user=request.user).last()
    if request.method == 'POST':
        form = FormList(data=request.POST)
        if form.is_valid():
            form.save()
            last_list = ListTask.objects.last()
            return render(request, 'main/tasks.html', {'list_data': last_list})
        else:
            print(form.errors)
    else:
        form = FormList(initial={"user": request.user})
    return render(request, 'main/lists.html', {'form_list': form, 'listas': listas, 'last_task': last_task})


@login_required
def shared(request):
    listas = ListTask.objects.all().order_by('-id')
    last_task = Item.objects.last()
    if request.method == 'POST':
        form = FormList(data=request.POST)
        if form.is_valid():
            form.save()
            last_list = ListTask.objects.last()
            return render(request, 'main/tasks.html', {'list_data': last_list})
        else:
            print(form.errors)
    else:
        form = FormList(initial={"user": request.user})
    return render(request, 'main/shared.html', {'form_list': form, 'listas': listas, 'last_task': last_task})


@login_required
def lists_delete(request, id):
    lista = ListTask.objects.filter(user=request.user, pk=id)
    if lista.exists():
        lista.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def tasks(request, id):
    try:
        list_data = ListTask.objects.get(pk=id)
        if request.method == 'POST':
            task_items = dict(
                filter(lambda val: 'task' in val[0], request.POST.items()))
            list_data.title = request.POST.get('title')
            list_data.description = request.POST.get('description')
            list_data.save()
            tasks = Item.objects.filter(list_task=list_data)
            if tasks.exists():
                tasks.delete()
            for key, val in task_items.items():
                new_item = Item(description=val, list_task=list_data)
                id = key[4:]
                if request.POST.get('check'+id):
                    new_item.done = True
                else:
                    new_item.done = False
                new_item.save()
        return render(request, 'main/tasks.html', {'list_data': list_data})
    except:
        return render(request, 'main/index.html')


@login_required
def task_update(request, id, done):
    old_item = Item.objects.filter(pk=id, list_task__user=request.user)
    if old_item.exists():
        update_item = old_item[0]
        if done == 'True':
            update_item.done = False
        else:
            update_item.done = True
        update_item.save()
    return redirect(request.META.get('HTTP_REFERER'))
