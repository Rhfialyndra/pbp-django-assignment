# 6<sup>th</sup> Assignment PBP
---
[Deployed Web](https://pbp-django-assignment.herokuapp.com/katalog/)
---
> Rahfi Alyendra G
> 2106705764

1. **Asynchronous vs Synchronous Programming**<br>
*Asyncrhonous programming* adalah paradigm yang memungkinkan kita untuk mengeksekusi 2 routine,subroutine atau process secara bersamaan (paralel), sedangkan *synchronous programming* mengharuskan kita untuk mengeksekusi hanya 1 routine, subroutine atau process pada interval waktu tertentu.
sebagai contoh, misalkan kita punya dua fungsi `task1()` dan `task2()`. Pada Synchronous programming jika kita ingin menjalankan kedua fungsi tersebut, maka eksekusi yang terjadi adalah `task1()`, lalu jika eksekusi `task1()` sudah selesai, kemudian `task2()` baru akan dieksekusi.
Pada *Asynchronous programming*, kedua task mungkin dieksekusi secara bersamaan.

2. **Event-driven Programming**<br>

Event adalah "interrupt" atau lebih simplenya lagi, sinyal yang diberikan kepada sebuah *current* proses untuk dihandle oleh *current* proses tersebut. event bisa berupa action explisit dari luar ataupun efek samping dari proses yang berlangsung.
dengan menggunakan *event-driven programming* kita bisa membuat logic dan fungsionalitas program yang lebih kompleks dan terarah. misalkan ketika terjadi event A, maka execute proses X dan proses Y. Lebih abstraknya lagi, kita bisa membuat program kita lebih interaktif dan high-performant.
Pada tugas kali ini, contoh event yang kita gunakan adalah event click (mouseclick).

```js

//1
$("#button").click(.....)

//2
$(document).ready(...)
```

kode nomor 1  menyatakan *"bind atau dengarkan event click yang dilakukan terhadap element html ber id 'button', kemudian jalankan .... jika memang terjadi event click"*.
kode nomor 2 menggunakan event yang serupa dengan "DOMContenLoad", artinya jika DOM sudah ter-render, maka lakukan ... .

3. **Async AJAX**<br>
	1. Ketika terjadi event (walaupun laman web telah ter-render), maka JavaScript akan membuat object XHR baru.
	2. objek XHR tersebut lantas dikirim ke server, kemudian responsenya diterima kembali oleh JavaScript
	3. response tersebut akan diolah, dan data laman web akan diperbarui (jika memang ada) oleh JavaScript tanpa harus merefresh.

	artinya, kita tetap bisa melakukan proses fetching data, tanpa harus memberhentikan proses yang sedang terjadi di laman web pada waktu tersebut.
	

4. **Implementation**<br>
	- include jquery cdn
	```js
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
	```
	- tulis kode js yang melakukan logic yang dinginkan, di sini saya meng-bind event "click" dan "DOMContentLoad"
	
	```js
	<script>
		function fetchData(){
			$.get(window.location.href+"json/", createCard)
		}

		$(document).ready(fetchData)
	</script>
	```
	TL;DR : jika document sudah ter-render, eksekusi fetchData() untuk mendapatkan data dari API tersebut.
	
	- lalu form create-task akan diubah ke dalam bentuk modal menggunakan class component dari daisyUI
	- buat view baru yang menerima POST request dan membuat Task baru dengan data yang disupply
	- handle POST request dari form dengan ajax
	
	```js
	<script>
	 $("#submit-button").click(function(e){
			e.preventDefault();
			let current = $('#form-create')
			var formData = current.serializeArray();	
			var url = e.currentTarget.action;
			
			const cleanData = {
				"csrfmiddlewaretoken" : formData[0].value,
				"title" : formData[1].value,
				"description" : formData[2].value,
			}
			
			$.ajax({
			type: "POST",
			url: "/todolist/add/",
			//contentType: "application/json; charset=utf-8",
			data:formData,
			success: data => {
				
				window.alert("berhasil menambahkan task!");
				formData[2].value = "";	
				$("#close-create-task-modal").click();
				$("#empty-task-notice").remove();
				appendCard(data[0]);
				
			},
			dataType: "json"
			});
		  });

	</script>
	```