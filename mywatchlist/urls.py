from django.urls import path
from mywatchlist.views import *;

app_name = 'mywatchlist'

urlpatterns = [
    path('html', show_mywatchlist_html, name='show_mywatchlist_html'),
    path('json', show_mywatchlist_json, name="show_mywatchlist_json"),
    path('xml', show_mywatchlist_xml, name="show_mywatchlist_xml"),
    path('xml/<int:id>', show_mywatchlist_xml_by_id, name="show_mywatchlist_xml_by_id"),
    path('json/<int:id>', show_mywatchlist_json_by_id, name="show_mywatchlist_json_by_id"),
]