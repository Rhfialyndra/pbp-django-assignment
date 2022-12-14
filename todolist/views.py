from django.contrib.auth import logout
from django.shortcuts import render;
from todolist.models import *;
from django.http import HttpResponse, HttpResponseRedirect;
from django.core import serializers;
from django.shortcuts import redirect;
from django.contrib.auth.forms import UserCreationForm;
from django.contrib import messages;
from django.contrib.auth import authenticate, login, models;
from django.contrib.auth.decorators import login_required;
from django.urls import reverse;
from .forms import TaskForm;
import datetime;
import json;


@login_required(login_url="/todolist/login/")
def show_todolist(request):
    context = {
        'size' : len(Task.objects.filter(user=request.user)),
        'nama': request.user.username,
    }
    #request.COOKIES['last_login']
    return render(request, "todolist.html", context)

@login_required(login_url="/todolist/login/")
def create_task(request):
    form = TaskForm();
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = models.User.objects.get(pk=request.user.id)
            obj.save()
            messages.success(request, "Berhasil membuat todo!")
    return render(request, "create-task.html", {"form" : form, "nama" : request.user.username} )


@login_required(login_url="/todolist/login/")
def create_task_json(request):
    
    if request.method == "POST":
        obj = Task();
        obj.user = request.user;
        obj.title = request.POST.get("title")
        obj.description = request.POST.get("description")
        obj.save();
        return HttpResponse(serializers.serialize("json", [obj]), content_type="application/json")
    
    return HttpResponse("only POST method allowed!");

@login_required(login_url="/todolist/login/")        
def get_all_task_json(request):
    if request.method == "GET":
        data = Task.objects.filter(user=request.user);
        return HttpResponse(serializers.serialize("json", data), content_type="application/json");
    return HttpResponse("Only GET method allowed!");   

@login_required(login_url="/todolist/login/")
def update_task(request, id):
    query = Task.objects.get(pk=id, user=request.user);
    if query is not None:
        query.is_finished = not query.is_finished;
        query.save();
        print(id, query.is_finished)
        return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url="/todolist/login/")
def delete_task(request, id):
    query = Task.objects.filter(pk=id, user=request.user).delete();
    return HttpResponse(reverse('todolist:show_todolist'))
    
@login_required(login_url="/todolist/login/")
def delete_task_ajax(request, id):
    query = Task.objects.filter(pk=id, user=request.user).delete();
    return HttpResponse("Berhasil menghapus task!")
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)
    
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    return response

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"));
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)