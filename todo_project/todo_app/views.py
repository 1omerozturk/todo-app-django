from django.shortcuts import render,HttpResponse,redirect
from .models import Todos
from .forms import ListForm
# Create your views here.

def index(request):
    if request.method=="POST":
        form=ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_list=Todos.objects.all()
            return render(request,"todo_app/index.html",{"todo_list":todo_list})

    else:
        todo_list=Todos.objects.all()
        return render(request,"todo_app/index.html",{"todo_list":todo_list})

def about(request):
    return render(request,"todo_app/about.html")

def create(request):
    if request.method=="POST":
        form=ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_list=Todos.objects.all()
            return render(request,"todo_app/create.html",{"todo_list":todo_list})

    else:
        todo_list=Todos.objects.all()
        return render(request,"todo_app/create.html",{"todo_list":todo_list})


def toggle_finished(request,todo_id):
    try:
        todo = Todos.objects.get(pk=todo_id)
        todo.finished = not todo.finished 
        todo.save()  
    except Todos.DoesNotExist:
        pass

    return redirect("index")

def delete(request,Todos_id):
    todo=Todos.objects.get(pk=Todos_id)
    todo.delete()
    return redirect("index")



def update(request,Todos_id):
    if request.method=="POST":
        todo_list=Todos.objects.get(pk=Todos_id)
        form=ListForm(request.POST or None,instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        todo_list=Todos.objects.all()
        return render(request,"todo_app/update.html",{'todo_list':todo_list})