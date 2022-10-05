# 2<sup>nd</sup> Assignment PBP
---
[Deployed Web](https://pbp-django-assignment.herokuapp.com/katalog/)
---
> Rahfi Alyendra G
> 2106705764

1. **MVT Pada Django**<br>
![MY MVT SCHEME](https://media.discordapp.net/attachments/854162996963311626/1019823246213910538/CamScanner_09-15-2022_11.12_1.jpg?width=669&height=498)
<br>

![MVT Django](https://media.discordapp.net/attachments/854162996963311626/1019216889420992532/unknown.png)
*taken from https://pythonguides.com/what-is-python-django/#django-architecture*

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

jalankan kembali runner pada `.github/workflow` tunggu beberapa saat, maka app kita telah terdeploy. <br>
<br>
<br>
<br>

# 3<sup>rd</sup> Assignment PBP

---
[Deployed Web](https://pbp-django-assignment.herokuapp.com/mywatchlist/html)
---

> Rahfi Alyendra G
> 2106705764

1. **The difference between JSON, XML and HTML?**<br>
Well, dari nama dan bentuknya sebenarnya sudah cukup jelas. XML dan HTML adalah markup language (bisa dilakukan berbagai operasi teks, seperti formatting), sedangkan JSON adalah notasi obyek JavaScript. XML lebih lazim digunakan dalam data/content delivery, sedangkan HTML lazimnya digunakan dalam data/content presentation. Kemudian, XML case sensitive, sedangkan HTML tidak. Namun, keduanya tetap menggunakan tag pembuka maupun penutup dalam mendefinisikan data/elemennya (markup lang)
JSON merupakan singkatan dari *JavaScript Object Notation*. JSON telah dijadikan standar dalam data delivery, sebab JSON simple, konsisten, dan "mudah" di parse.
Berbeda dengan Markup, JSON menotasikan datanya sebagai dictionary key-value pairs. JSON bisa menyimpan 6 tipe data (JS primitive), yakni string, integer, boolean, object, array, null.

2. **Why do we need data delivery for our platform?**<br>
Jika Platform yang kita buat menyimpan/menampilkan banyak data pada client-side, tentu saja kita tidak mau menyimpan seluruh data tersebut secara statis pada aplikasi kita, sebab akan memakan banyak memori dan justru akan memperlambat kinerja aplikasi kita.
Lalu, *For the sake of reusability*. Kita bisa menggunakan database/backend yang sama untuk beberapa app pada platform yang berbeda, oleh karena itu, dibuatlah skema data delivery dari 1 sumber yang sama (sebaiknya dan seharusnya) dengan menggunakan JSON. dengan begitu, kita tidak perlu membuat backend-side untuk masing-masing app yang berbeda.

3.**Implementation**<br>
- create new app

```python
3(in active env)
django-admin startapp mywatchlist
```

add `mywatchlist` to INSTALLED_APPS on `settings.py`.

- add routing.

add codes below inside base urls.py (inside the project_django folder)

```python
path("/mywatchlist", include("mywatchlist.urls"))
```

- create new model

go to `/mywatchlist/models.py`, and create new model MyWatchList

```python
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator ;
class MyWatchList(models.Model):
    title = models.CharField(max_length=69);
    release_date = models.CharField(max_length=10);
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]);
    description = models.TextField(max_length=500);
    watched = models.BooleanField(default=False)
```

**Screenshots**

1. HTML<br>
![HTML SS](https://media.discordapp.net/attachments/854162996963311626/1021746908470980638/unknown.png?width=886&height=498)<br>

2. JSON<br>
![JSON ss](https://media.discordapp.net/attachments/854162996963311626/1021747008047939584/unknown.png?width=886&height=498)

3. XML<br>
![XML ss](https://media.discordapp.net/attachments/854162996963311626/1021747085328011294/unknown.png?width=886&height=498)

<br>
<br>

# 4<sup>th</sup> Assignment PBP
---
[Deployed Web](https://pbp-django-assignment.herokuapp.com/todolist/)
---
> Rahfi Alyendra G
> 2106705764

1. **The use of CSRF TOKEN on POST form**<br>
CSRF (Cross Site Request Forgery) token adalah token yang digunakan sebagai "autentikator" atau "verifier", ketika request yang masuk ke platform, berasal dari luar local(host).
CSRF token bisa dikatan mirip sebagai api_key, dimana request harus memuat token yang sesuai dengan token yang  ter-record platform (server). dengan menerapkan CSRF token, platform server tidak akan menerima dan menjalankan request dari sembarang client. 
Oleh karena itu, platform semakin aman dari serangan pihak luar, baik yang disengaja maupun tidak.
Pada django, jika kita tidak memuat `{% csrf_token %}`, maka request POST yang kita kirim tidak memiliki token. 
django akan mereturn http status code 403, yakni forbidden, karena menganggap request yang kita kirim `malicious` (tidak bisa dipercaya).


2. Other ways to create forms beside  {{ form.as_table }}<br>
pada django, ada 2 cara lain (yang saya ketahui ofc) dalam membuat form, yakni dengan membuat html form secara manual, atau membuat instance `Form` baru pada `forms.py` dengan memanfaatkan `ModelForm`.
untuk membuat html form secara manual, kita hanya perlu membuat elemen `<form>` dengan action endpoint yang seusai, dan method (tidak terbatas pada) POST.
lalu untuk setiap input field, harus disertakan juga `<label>` dengan attribut `name` dan `for` respectively yang merujuk ke field Model yang sama. 
Jika, kita ingin membuat Form baru pada `forms.py`, kita bisa memanfaatkan class ModelForm.
```python
from todolist.models import *;
from django.forms import *;

class TaskForm(ModelForm):
    class Meta:
        model = Task;
        fields = ["title", "description"]
```
dengan menggunakan ModelForm, kita seakan-akan membuat form yang langsung terhubung secara khusus ke model terkait. lalu kita juga bisa mendefinisikan field-field yang diperlukan sebagai input.

untuk form manapun, kita tetap harus menambahkan button dengan type dan value "submit" agar data kita bisa terpost.

3. **How does formData get stored at the database?**<br>
django form me-map input field HTML ke field/attribute pada model. untuk setiap instance `Form`, maka form tersebut sudah memiliki model yang terikat atau django akan membuat models dan record baru setiap form tersubmit.
ketika user mengklik submit, maka django akan melakukan validasi terhadap form. jika valid, form akan dikonversi ke dalam object Model, lalu disimpan sebagai record Model baru ke database. 
dengan begitu, data baru yang masuk tersebut bisa di fetch dan ditampilkan sebagai data di html.

 4. **Implementasi**
- buat app baru `todolist`
- buat model baru pada `todolist`, yakni model Task dan sertakan user sebagai attribute dengan tipe foreign key dan `User` sebagai valuenya
```python
from todolist.models import *;
from django.forms import *;

class TaskForm(ModelForm):
    class Meta:
        model = Task;
        fields = ["title", "description"]
```
- buat function baru pada views yang mereturn html `todolist` dan `create-task`. tambahkan decorator `login_required` sehingga hanya user yang logged in yang bisa mengakses.
```python
@login_required(login_url="/todolist/login/")
def show_todolist(request):
    context = {
        'todo_list': Task.objects.filter(user=request.user),
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
    return render(request, "create-task.html", {"form" : form} )
```
context.todo_list merupakan array dari Task yang telah kita filter, di mana `Task.user == request.user`.
lalu `create_task` akan menerima request POST dari user, memvalidasi form kemudian menyimpan ke dalam database.

- definisikan routing pada `urls.py`
```python
# this is todolist/urls.py

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
    path('delete_task/<int:id>', delete_task, name='delete_task')
]
```

```python
# this is project_django/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls')),
    path('mywatchlist/', include('mywatchlist.urls')),
    path('todolist/', include('todolist.urls'))
]
```

- masukan `todolist` pada `INSTALLED_APPS` di settings.py
- ubah value dari `release` pada Procfile menjadi : 
```sh
release: sh -c 'python manage.py makemigrations && python manage.py migrate && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_mywatchlist_data.json'

```
- push ke commit ke github, runner akan berjalan otomatis dan web akan terdeploy.


# 5<sup>th</sup> Assignment PBP
---
[Deployed Web](https://pbp-django-assignment.herokuapp.com/todolist/)
---
> Rahfi Alyendra G
> 2106705764

1. **inline vs internal vs external CSS**<br>
- inline
```html
<button style="padding:20px;background-color:blue;border-radius:10px;">click me</button>
```
pros : Mudah dalam menganalisa styling (karena langsung tau element yang mana).
cons : tidak enak dipandang, terlalu ruwet. memerlukan banyak penulisan code.

- internal
```html

<head>
	<style>
	.classname {
		font-weight : bold;
		font-size : 100px;
	}
	</style>
</head>

<body>
....
</body>
```
pros : lebih enak dipandang dibandingkan inline. efisien karena reusable.
cons : kalau banyak element dan selector, cukup bingung dalam men-trace reference dari setiap styling.

- external
```css
// file berbeda dari html

	.classname {
		font-weight : bold;
		font-size : 100px;
	}
```
pros : separation of concern, yaitu "context" dari setiap file dipisahkan sesuai dengan fungsinya sehingga code lebih clean. efisien karena reusable.
cons : kalau banyak element dan selector, cukup bingung dalam men-trace reference dari setiap styling. memperbanyak file pada project dir structure.

Ya, bedanya adalah peletakan code css pada saat penggunaannya. Tak hanya itu, terdapat perbedaan pada tingkat prioritas, yakni
    1. Inline style
    2. External dan internal style sheets
    3. Browser default

2.**Tags HTML**<br>
Ini Saya sudah bikin markdownya yang cukup comprehensive, saya sisipkan link saja ya https://github.com/Rhfialyndra/resource-sbf-2022/blob/master/Frontend/Basic%20Frontend%20Core.md

3. **Tipe-tipe Selector CSS**
  - Element Selector
  ```css
	h1 {
	//css property:val; goes here
	
	}
  ```
  langsung mengselect/me-refer ke elmenet htmlnya.
  
  - Class Selector
  ```css
	.NAMA_CLASS {
	//css property:val; goes here
	
	}
  ```
  merefer ke element html yang telah diberi attribute class dengan value `NAMA_CLASS` (non-unique).
  
  - id Selector
  ```css
	#NAMA_ID {
	//css property:val; goes here
	
	}
  ```
  merefer ke element html yang telah diberi attribute id dengan value `NAMA_CLASS` (harus unique).
  
  Selain selector di atas, terdapat beberapa *combinators* yang bisa digunakan bersamaan dengan selector, yakni
    - Descendant selector (space) --> `div p {} == Selects all <p> elements inside <div> elements`
    - Child selector (>) --> `div > p {} ==	Selects all <p> elements where the parent is a <div> element`
    - Adjacent sibling selector (+) --> `div + p {} ==	Selects the first <p> element that is placed immediately after <div> elements`
    - General sibling selector (~) `p ~ ul 	Selects every <ul> element that is preceded by a <p> element`
	
4. **Implementation**<br>
	- menggunakan tailwindcss, daisyUI dan VANTA.js.
	
	import *Content Delivery Network* (CDN) dari tailwindcss, daisyUI dan VANTA.json
	
	```html
		<head>
			<link href="https://cdn.jsdelivr.net/npm/daisyui@2.31.0/dist/full.css" rel="stylesheet" type="text/css" />
			<script src="https://cdn.tailwindcss.com"></script>
			<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r121/three.min.js"></script>
			<script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.clouds.min.js"></script>
		</head>
	```
	
	- gunakan class component navbar dari daisyUI.
	- gunakan class component card dari daisyUI untuk membuat card task todolist.
	- terapkan styling sesuka hati
	- buat tampilan menjadi responsive dengan media breakpoint tailwindcss.
	- buat function untuk VANTA 3d wallpaper
	```html
	<head>
		<script>
            window.addEventListener("DOMContentLoaded", () => {

                

                VANTA.CLOUDS({
                    el: "#VANTA-CLOUDS",
                    mouseControls: true,
                    touchControls: true,
                    gyroControls: false,
                    minHeight: 200.00,
                    minWidth: 200.00,
                    skyColor: 0x4196c8,
                    cloudShadowColor: 0x505664,
                    sunColor: 0xbb8b4d,
                    sunGlareColor: 0xeb7b53,
                    sunlightColor: 0xb1804f,
                    speed: 0.80,
                    backgroundAlpha : 0.0
                })

            })
        </script>
	</head>
	```
	- terapkan selector untuk live wallpaper tsb
	```html
	<body id="VANTA">
		.
		.
		.
		.
		<div id="VANTA-CLOUDS" class="-z-10 fixed top-0 w-screen min-h-screen"></div>
	</body>
	```
	