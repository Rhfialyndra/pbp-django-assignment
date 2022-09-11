from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(request):
    context = {
        'item_list' : CatalogItem.objects.all(),
        'full_name' : 'Rahfi Alyendra G',
        'student_id' : '2106705764',
    }
    return render(request, 'katalog.html', context);
