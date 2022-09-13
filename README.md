# Lab 1 Assignment PBP

---

[Deployed Web](https://pbp-django-assignment.herokuapp.com/katalog/)

---

> Rahfi Alyendra G
> 2106705764


1. **MVT Pada Django**<br>
![MVT Django](https://media.discordapp.net/attachments/854162996963311626/1019216889420992532/unknown.png)

django menggunakan paradigm Model-View-Template pada frameworknya. 
`urls.py` bertugas untuk "mengatur" route/endpoint pada app kita. setiap request akan diteruskan ke `views.py` sesuai dengan pattern yang tertera pada `urls.py`.
perilaku views mirip dengan API (REST). `views.py` akan melakukan "pengambilan" data dari `models.py` yang sesuai dengan request, lalu akan menginjeksi data tersebut ke template response, dalam kasus ini `katalog.html` sehingga akan dikembalikan laman web dengan data yang sesuai.

<br>

2. **Why do wee need venv to run django? what will happen otherwise?**<br>
*virtual environment* sejatinya berfungsi sebagai *env* yang bersifat `"local"/scoped`
pada djangoapp tersebut. 
dengan menggunakan *virtual environment*, maka kita bisa mengikat segala *dependencies* kita hanya kepada venv djangoapp tersebut.
Dengan begitu, kita tidak menginstall *deps* yang berlebih dan tidak berguna secara global pada device yang kita gunakan.
Sebenarnya, tanpa menggunakan *virtual environment*, kita juga dapat membangun serta menjalankan djangoapp kita, tetapi kita akan kesusahan ketika mencoba untuk menjalankan djangoapp kita pada *device* yang berbeda atau bahkan ketika kita mencoba untuk men-*deploy* djangoapp kita ke VPS.
Hal ini terjadi, karena mungkin saja versi *deps* (termasuk djangonya sendiri) berbeda-beda tiap *device* sehingga bisa menyebabkan *conflict* pada *development app*.
Maka dari itu, *best practice* saat membangun djangoapp , ialah dengan menggunakan *virtual environment*.

<br>

3. **Implementation**<br>
- Setting up the venv
Pertama, kita install *venv* dulu dengan command `py -m venv <NAMA_ENV>`. Saya menggunakan "env" sebagai namanya.
Lalu, kita activate venv tersebut, dan install segala deps yang diperlukan dengan command `pip install -r requirements.txt`.

- starting the djangoapp
pergi ke root dir kita, lalu kita jalankan command `py manage.py makemigration` dan `py manage.py migrate`, untuk menginisiasi "database".
lalu, kita load data pada /fixtures ke database dengan command `py manage.py loaddata <FILE_DATA_FIXTURES>`.
jalankan localserver dengan command `py manage.py runserver <OPTIONAL_IP(default to localhost)>`.

- views.py
Sekarang kita perlu membuat views sebagai "API" untuk menerima reqs dan mengembalikan response.
pada `views.py` kita lakukan import models pada app `katalog`. lalu kita harus membuat fungsi yang menerima req.

```python
from katalog.models import ItemCatalog;

def show_catalog(request):
	context = {
	'item_list' : ItemCatalog.objects.all(),
	'nama' : blabalabla,
	'id' : balbalabla
	}
	return render(request, 'katalog.html', context )

```
TL;DR  : fungsi di atas akan menerima request, lalu mengembalikan response katalog.html, dengan data `context`.


- katalog.html

html ini akan dikembalikan sebagai response, maka dari itu kita perlu melakukan mapping data dari `show_catalog`,
dengan menambahkan row-data pada tabel.

```
{% for item in item_list %}
	<tr class="table-catalog-data">
        <td>{{item.item_name}}</td>
        <td>Rp{{item.item_price}}</td>
        <td>{{item.item_stock}}</td>
		<td>{{item.rating}}</td>
        <td>{{item.description}}</td>
        <td><a href={{item.item_url}}>{{item.item_url}}</a></td>
    </tr>
{% endfor %}
```

TL;DR : classic python for loop, and map the data onto html element.


- urls.py
pada folder katalog , kita harus mendefinisikan routing untuk folder tersebut, pada `urls.py`.

```python
from katalog.views import show_catalog

app_name = 'katalog'

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
]
```

lalu, pada `urls.py` di root dir, kita harus menginclude semua route untuk semua app yang ada.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls'))
]

```
TL;DR : includes and specify routes and endpoint names, for every app. (in this case baseURL/katalog is used to access the katalog.html page)

- DEPLOYMENT
Kita menggunakan heroku. login ke heroku, dan buat app baru. Lalu, copy `API-KEY`yang tertera pada profile heroku kita.
buat repo baru, lalu push django project kita. pergi ke site settings, lalu tambahkan site's secret, yakni :

```
HEROKU_API_KEY : SESUAI_YANG_DI_COPY,
HEROKU_APP_NAME : SESUAI_NAMA_HEROKUAPP_YANG_DIBUAT
```
jalankan kembali runner pada `.github/workflow` tunggu beberapa saat, maka app kita telah terdeploy.