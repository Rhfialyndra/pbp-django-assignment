from todolist.models import *;
from django.forms import *;

class TaskForm(ModelForm):
    class Meta:
        model = Task;
        fields = ["title", "description"]

