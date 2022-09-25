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


@login_required(login_url="/todolist/login/")
def show_todolist(request):
    context = {
        'todo_list': Task.objects.all(),
        'size' : len(Task.objects.all()),
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
    return render(request, "create-task.html", {"form" : form} )
    
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