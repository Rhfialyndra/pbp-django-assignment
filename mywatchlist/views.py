from django.shortcuts import render
from mywatchlist.models import MyWatchList;
from django.http import HttpResponse;
from django.core import serializers;



# Create your views here.

def show_mywatchlist_html(request):
    context = {
        'watchlist' : MyWatchList.objects.all(),
        'full_name' : 'Rahfi Alyendra G',
        'student_id' : '2106705764',
        'watched_more_than_half_of_the_wishlist' : len(MyWatchList.objects.filter(watched=True)) >= len(MyWatchList.objects.filter(watched=False))
        
    }
    print(len(MyWatchList.objects.filter(watched=True)), len(MyWatchList.objects.filter(watched=False)))
    return render(request, 'mywatchlist.html', context);

def show_mywatchlist_xml(request):
    data = MyWatchList.objects.all();
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml");
    
def show_mywatchlist_json(request):
    data = MyWatchList.objects.all();
    return HttpResponse(serializers.serialize("json", data), content_type="application/json");    

def show_mywatchlist_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id);
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml");
    
def show_mywatchlist_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id);
    return HttpResponse(serializers.serialize("json", data), content_type="application/json"); 