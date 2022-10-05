from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/lista.html', {'tasks':tasks})

def teste(request):
    return HttpResponse('teste')

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html',{'form' : form})


def editar(request):
    return render(request, 'tasks/editar.html')


def deleteTask(request,id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('/')