from django.shortcuts import render,redirect,reverse
from .models import Todo
from .forms import TodoCreateForm
from django.http import HttpResponseRedirect 

# Create your views here.
def todo_home(request):
    todos = Todo.objects.all()
    return render(request,'todo/home.html',
                        {'todos':todos})

def todo_detail(request,id):
    todo = Todo.objects.get(id=id)
    return render(request,'todo/detail.html',
                            {'todo':todo})

def todo_create(request ):
    if request.method == 'POST':
        form =TodoCreateForm(request.POST)
        if form.is_valid():
            todo = form.save()

        return redirect('detail',todo.id)
    else :
        form = TodoCreateForm()
    return render(request,'todo/create.html',{'form':form})

def todo_update(request,id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoCreateForm(request.POST,instance=todo)
        if form.is_valid():
            form = form.save()
            return redirect('detail',todo.id)
    else :
        form = TodoCreateForm(instance=todo)
    return render(request,'todo/update.html',
                    {'form':form})

def todo_delete(request,id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return HttpResponseRedirect(reverse('home'))
    return render(request,'todo/delete.html',{'todo':todo})