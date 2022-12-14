from django.urls import path
from todolist.views import *;

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('login/', login_user, name="login_user"),
    path('register', register, name="register"),
    path('logout/', logout_user, name='logout_user'),
    path('create-task/', create_task, name='create_task'),
    path('update_task/<int:id>', update_task, name='update_task'),
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    path('delete/<int:id>', delete_task_ajax, name='delete_task_ajax'),
    path('json/', get_all_task_json, name="get_all_task_json"),
    path('add/', create_task_json, name="create_task_json"),
]