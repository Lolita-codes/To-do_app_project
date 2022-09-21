from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import ToDo
from .forms import ToDoForm
import datetime


def index(request):
    form = ToDoForm()
    today = datetime.datetime.now()
    todo_list = ToDo.objects.order_by('id')
    return render(request, 'todo/index.html',
                  {'todo_list': todo_list, 'form': form, 'date': today})


@require_POST
def add_item(request):
    form = ToDoForm(request.POST)
    if form.is_valid():
        new_item = ToDo(item=form.cleaned_data['item'])
        new_item.save()

    return redirect('index')


def completed_item(request, todo_id):
    task = ToDo.objects.get(pk=todo_id)
    task.completed = True
    task.save()
    return redirect('index')


def delete_completed(request):
    all_completed = ToDo.objects.filter(completed=True).delete()
    return redirect('index')


def delete_all(request):
    all_items = ToDo.objects.all().delete()
    return redirect('index')
