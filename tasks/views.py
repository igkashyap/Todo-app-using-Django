from django.shortcuts import render, redirect
from .models import tasksdb
from .form import tasksform

# Create your views here.
def index(request):
    tasks = tasksdb.objects.all()
    form = tasksform()
    if request.method=="POST":
        form = tasksform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {'tasks':tasks, 'form':form}
    return render(request,'tasks/index.html', context)

def updatetask(request, pk):
    tasks = tasksdb.objects.get(id=pk)
    form = tasksform(instance=tasks)
    if request.method=="POST":
        form = tasksform(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('index')    
    context = {'form':form}
    return render(request, 'tasks/update.html', context)

def deletetask(request, pk):
    tasks = tasksdb.objects.get(id=pk)
    if request.method=="POST":
        tasks.delete()
        return redirect('index')
    context = {'tasks':tasks}
    return render(request,'tasks/delete.html',context)    