from django.urls import path
from todolist.views import *;

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('login/', login_user, name="login_user"),
    path('register', register, name="register"),
    path('logout/', logout_user, name='logout_user'),
    path('create-task/', create_task, name='create_task'),
]