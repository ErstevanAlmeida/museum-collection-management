## Nama    : Erstevan Laurel Lucky Almeida
## NPM     : 2206082493
## Kelas   : PBP - E

<hr>

## Tugas 2 : Implementasi MVT pada Django

- [x] Membuat sebuah proyek Django baru.
- [x] Membuat aplikasi dengan nama main pada proyek tersebut.
- [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- [x] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    - name sebagai nama item dengan tipe CharField.
    - amount sebagai jumlah item dengan tipe IntegerField.
    - description sebagai deskripsi item dengan tipe TextField.
- [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- [x] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Jawab:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
    : Pertama-tama saya membuat proyek Django baru yang saya beri nama 'museum_collection_management'. Hal itu dapat saya lakukan dengan 'django-admin startproject museum_collection_management. Kemudian, membuat aplikasi yang bernama main dengan syntax python manage.py startapp main. Selanjutnya, melakukan routing dan membuat model dalam aplikasi main. Lalu, pada saat membuat model, saya juga membuat atribut-atribut, seperti name, type, collection, year, amount, dan description. setiap attribut memiliki tipe-nya tersendiri. Seperti contohnya, name, collection, dan type memiliki tipe CharField. Sedangkan year dan amount memiliki tipe IntegerField. Lalu, description saya membuatnya dengan tipe TextField.

    : Kemudian, membuat fungsi pada views.py pada aplikasi main yang bertujuan untuk menyimpan data yang akan digunakan di web nanti. Selanjutnya melakukan routing kembali agar dapat memetakan fungsi yang telah dibuat. Langkah yang terakhir, adalah melakukan deployment dengan menggunakan Adaptable.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!
    : Client request -> urls.py -> views.py -> models.py -> Template (HMTL file) -> Response -> Client

    : Pertama-tama, client akan melakukan request dengan cara membuka web browser dan mengetik url aplikasinya. Kemudia Django menerima request tersebut serta menghubungkan url yang diminta dengan views yang sesuai. Hal tersebut dapat terjadi dengan menggunakan url patterns yang sudah di-assign sebelumnya di urls.py. Selanjutnya, Django akan mengarahkan request tersebut kepada views yang sesuai yang ada pada views.py. Di dalam views.py terdapat fungsi yang digunakan untuk mengelola data.
    
    : Jika fungsi yang terdapat pada views.py memerlukan data dari database, maka kita pelru mendefinisikan terlebih dahulu struktur data setiap variabel pada models.py. Selanjutnya, beralih ke HTML Template yang digunakan untuk membuat tampilan yang akan ditampilkan. HTML Template sendiri memiliki fungsi untuk memisahkan pengerjaan UI dengan fungsi-fungsi interaksi yang ada di belakang tampilannya. Terakhir, Django akan merespons dan menggabungkan HTML Template dengan data yang ada pada views.py. Respons yang dihasilkan akan dikirim kembali ke tampilan browser pengguna.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    : Virtual environement sangat berguna untuk mengisolasi proyek yang sedang dikerjakan. Hal ini dapat membuat kita menggunakan berbagai kebutuhan yang kita butuhkan untuk membangun sebuah proyek. Karena, terkadang setiap proyek yang kita kerjakan membutuhkan kebutuhan yang berbeda-beda antar proyeknya. Maka dari itu, kita membutuhkan virtual environment dalam membangun proyek ini.

    : Sebenarnya, kita akan tetap bisa membuat dan membangun aplikasi web Django tanpa menggunakan virtual environment. Namun, hal tersebut tidak dianjurkan karena banyak sekali keunggulan jika kita menggunakan virtual environment. Seperti, kebersihan, keamanan, dan juga untuk menghindari konflik antar package.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya!
    : Model View-Controller (MVC) merupakan pola desain atau arsitektur perangkat lunak yang membagi aplikasi menjadi tiga komponen utama. Model merupakan komponen yang bertugas dalam pengelolaan data. View yang bertugas untuk mengatur tampilan (UI) pada sebuah perangkat lunak. 

    : Model View-Template (MVT) merupakan sebuah pola yang mirip dengan MVC. Namun, pola ini paling sering digunakan pada Django. Hal yang membedakan MVT dengan MVC adalah pada komponen View. Pada MVT, komponen View tidak digunakan untuk mengatur UI. Template yang akan mengatur UI dari perangkat lunak tersebut.

    : Model View-ViewModel (MVVM) merupakan sebuah pola desain untuk pengembangan perangkat lunak. Model dan View yang terdapat di MVVM ini sama saja seperti Model dan View pada MVC dan MVC. Namun, terdapat komponen baru yakni ViewModel yang digunakan untuk mengatur logika dari presentasi sebuah web agar menjadi lebih efisien.

    : Salah satu perbedaannya, yakni dalam aspek implementasinya. MVC kerap kali digunakan pada desain software yang lebih umum. MVT dikerjakan pada framework Django. MVVM digunakan ketika sedang membuat desain yang lebih kompleks karena adanya VM yang dapat membuat logika presentasi menjadi lebih efisien. 

<hr>

## Tugas 3: Implementasi Form dan Data Delivery pada Django

- [x] Membuat input form untuk menambahkan objek model pada app sebelumnya.
- [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

1. Apa perbedaan antara form POST dan form GET dalam Django?
    : Terdapat beberapa perbedaan antar POST dan GET pada Django. Beikut adalah perbedaan-perbedaannya:
    : * Method POST seringkali digunakan untuk mengirim data ke database. Sedangkan, method GET seringkali digunakan hanya untuk mengambil data.
    : * Ketika sebuah data dikirim menggunakan method POST, maka data tersebut tidak akan muncul di url. Namun, jika data tersebut dikirim menggunakan method GET, maka data tersebut akan muncul di url. Hal ini berkaitan dengan keamanan data pengguna.
    : * Pada method POST tidak memiliki batasan jumlah karakter yang dikirimkan. Sedangkan, pada method GET memiliki batasan jumlah karakter yang dikarenakan harus dituliskan ke url dan url memiliki batasan karakter.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    : Dari segi tampilannya, 
    : * XML memiliki struktur yang lebih hierarkis, namun agak sulit untuk dibaca oleh manusia.
    : * JSON menampilkan data yang lebih ringan dan lebih mudah untuk dibaca oleh manusia maupun mesin. Hal tersebut dikarenakan JSON memiliki struktur berupa objek.
    : * HTML seringkali digunakan oleh developer untuk membuat dan merancang tampilan dari sebuah web, seperti menentukan posisi, dan sebagainya.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    : Karena JSON memiliki struktur yang lebih ringkas dan lebih mudah untuk dibaca oleh manusia. Data pada JSON juga disusun berdasarkan objeknya sehingga dapat lebih mudah untuk diidentifikasi oleh developer.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    : Hal pertama yang saya lakukan pastinya adalah melanjutkan proyek yang sudah saya kerjakan pada minggu sebelumnya. Kemudian, saya membuat file baru bernama `base.html` untuk membuat template file HTML yang dapat saya digunakan sebagai base untuk setiap file HTML saya. Lalu, memasukkannya pada `settings.py` dan merevisi berkas `main.html` saya. Selanjutnya, saya membuat form untuk menginput data pada berkas baru `forms.py` serta menghubungkannya denganproyek yang tengah saya buat dengan menambahkannya pada `views.py`. Pada berkas tersebut, saya membuat fungsi baru bernama `create_collection` yang akan digunakan untuk menambahkan  baru serta menambahkan syntax baru pada fungsi `show_main` (termasuk counter untuk menghitung jumlah koleksi yang ada). Hal ini akan digunakan untuk menampilkan produk tersebut.

    : Setelah itu, saya menambahkan path url untuk `create_collection` pada `urls.py`. Kemudian, membuat berkas HTML baru untuk menambahkan koleksi ke database. Lalu, mengubah output pada berkas `main.html` untuk bisa mengiterasi koleksi yang ada di database. Selanjutnya, membuat sebuah function baru pada `views.py` yang bertujuan untuk mengembalikan data dalam bentuk XML. Hal yang sama juga saya lakukan untuk mengembalikan data dalam bentuk JSON, serta mengakses berdasarkan ID-nya baik pada XML, maupun JSON. Terakhir, mengakses di Postman dan melakukan push ke GitHub.

Akses menggunakan PostMan:
* HTML
<img width="250" alt="Tugas3-pbp-html 1" src="https://github.com/ErstevanAlmeida/museum-collection-management/assets/119406929/47d7488f-5320-44d3-8606-6e077e3fcef0">
<img width="250" alt="tugas3pbphtml2" src="https://github.com/ErstevanAlmeida/lab0/assets/119406929/ab9d6b82-e727-4483-82b3-b6df094a162e">
<img width="250" alt="tugas3pbphtml3" src="https://github.com/ErstevanAlmeida/lab0/assets/119406929/12be3371-4de9-4c9f-ba14-b17175fe8a40">

* XML
<img width="1541" alt="tugas3pbpxml" src="https://github.com/ErstevanAlmeida/lab0/assets/119406929/117d7f1f-e8bc-4767-b4e6-2bd59baf4608">

* JSON
<img width="1541" alt="tugas3pbpjson" src="https://github.com/ErstevanAlmeida/lab0/assets/119406929/f13104eb-b632-4459-b455-e0982741cbac">

* XML by ID
<img width="1514" alt="tugas3pbpxmlid" src="https://github.com/ErstevanAlmeida/lab0/assets/119406929/9f27ae8c-3253-450a-ae1b-b5c0d9db7469">

* JSON by ID
<img width="1543" alt="tugas3pbpjsonid" src="https://github.com/ErstevanAlmeida/lab0/assets/119406929/41e17e74-86b5-4895-a9a1-8c26a94c05d9">

<hr>

## Tugas 4 : Implementasi Autentikasi, Session, dan Cookies pada Django

- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
- [x] Menghubungkan model Item dengan User.
- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
    : `UserCreationForm` adalah impor formulir bawaan Django yang digunakan untuk membuat formulir pendaftaran. 

    : Kelebihan : Memudahkan *developer* dalam membuat formulir registrasi tanpa harus membuatnya dari awal. Dapat memvalidasi input secara automatis.

    : Kekurangan : Sulit untuk mengkostumisasi UI-nya karena `UserCreationForm` bukan difokuskan untuk estetika, tetapi fungsinya. Sulit untuk menambahkan input seperti nama lengkap, nomor handphone, dll, karena input yang disajikan hanya berupa Username dan Password. 

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    : Autentikasi merupakan proses untuk identifikasi setiap pengguna yang akan login dengan melakukan kecocokan data input dengan data yang ada di basis data. Sedangkan, otorisasi merupakan proses perizinan pengguna untuk melihat data-data yang telah dimasukkan pada akun pengguna tersebut. Proses ini terjadi setelah data input pengguna terverifikasi pada proses autentikasi.

    : Keduanya menjadi penting karena salah satunya adalah faktor keamanan. Hal ini dikarenakan pada web tersebut hanya akan menampilkan data yang telah dibuat sendiri. Kedua langkah tersebut memastikan data yang bersifat privasi hanya akan ditampilkan ketika akun yang memasukkan data tersebut berhasil login.

3. Apa itu *cookies* dalam konteks aplikasi web, bagaimana Django menggunakan *cookies* untuk mengelola data sesi pengguna?
    : *Cookies* merupakan kumpulan informasi dan/atau data yang diperoleh ketika melakukan penelusuran lewat situs web. Data yang disimpan pada *cookies* dapat diakses kembali ketika kita akan melakukan penelusuran kembali pada waktu yang akan datang.

    : Django menggunakan *cookies* untuk menyimpan informasi pada website dan merujuk yang disimpan pada web tersebut. Nantinya, web akan menyimpan data yang penting, seperti informasi login, dan sebagainya.

4. Apakah penggunaan *cookies* aman secara *default* dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    : *By default, cookies* aman digunakan dalam pengembangan web. Namun, karena *cookies* dapat menyimpan data-data yang cukup penting seperti Username dan Password pengguna, maka memungkinkan adanya *data breach* ketika halaman web tersebut "diserang".

5. Jelaskan bagaimana cara kamu mengimplementasi *checklist* di atas secara *step-by-step*
    : Hal pertama yang saya lakukan adalah membuat fungsi registrasi yang memanfaatkan `UserCreationForm` pada `views.py`. Fungsi ini memperoleh data akun yang telah dibuat dan akan langsung masuk ke basis data akun tersebut pada halaman utama. Fungsi tersebut akan diimplementasikan  pada file HTML yang baru dibuat, Kemudian menaruh url pada `urls.py`. 
    
    : Kemudian pada login, saya juga membuat fungsi loginnnya terlebih dahulu. Lalu, membuat file HTML baru dan mengimplemetasikan fungsi tersebut serta menruhnya pada `urls.py`. Saya juga membuat fungsi logout yang akan mengembalikan ke halaman login dari website tersebut.

    : Selanjutnya, saya membuat akun dan memasukkan data pada create collection site. Kemudian, menghubungkan collection yang saya punya dengan user agar user yang dapat melihat hanya user yang login pada akun tersebut. Terakhir, menampilkan nama akun dan sesi terakhir login pada file HTML halaman utama. 

<hr>

## Tugas 5 : Desain Web menggunakan HTML, CSS dan Framework CSS

- [x] Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut
- [x] Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
- [x] Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.

1. Jelaskan manfaat dari setiap *element selector* dan kapan waktu yang tepat untuk menggunakannya! <br>
    : - Elemen Selector digunakan untuk mengkostumisasi elemen tertentu secara keseluruhan, misal penentuan ukutan font pada p atau h1. Selector ini dapat digunakan ketika ingin menerapkan kostumisasi pada semua elemen yang sama.
    : - Class Selector digunakan untuk menerapkan kostumisasi untuk *class* tertentu. Selector ini dapat digunakan ketika ingin menerapkan tampilan yang sama pada elemen-elemen yang tergolong serupa pada tampilan dan fungsionalitas.
    : - ID Selector digunakan untuk menerapkan kostumisasi terhadap elemen : yang lebih spesifik lagi. Selector ini dapat digunakan ketika ingin menerapkan kostumisasi pada elemen yang unik. Namun, minusnya adalah karena ID memiliki sifat yang unik, maka *selector* ini tidak bisa dipakai berulang kali.
    : - Attribut Selector digunakan untuk memilih elemen berdasarkan nilai atributnya. Selector ini biasanya digunakan untuk mengkostumisasi elemen tertentu yang memiliki atribut yang lebih spesifik.

2. Jelaskan HTML5 Tag yang kamu ketahui!<br>
    : `<title>` : mengatur judul yang ditampilkan pada halaman website.
    : `<header>` : menunjukkan bagian awal dokumen.
    : `<table>` : tag untuk membuat tabel.
    : `<thead>`, `<tbody>`, `<tfoot>` : mengelompokkan tag di dalam tabel sesuai dengan pembagiannya.
    : `<br>` : menambahkan baris kosong atau break antar elemennya.
    : `<h1>`, `<h2>`, `<h3>`, ... : memberikan tingkatan tag-heading.
    : `<p>` : mengidentifikasikan paragraf pada  website.
    : `<a>` : membuat tautan ke halaman web lain.
    : `<li>` : membuat list.
    : `<ul>` : membuat daftar/list yang tak terurut.
    : `<div>` : mengelompokkan elemen-elemen HTML.
    : `<button>` : tag untuk membuat button / tombol.
    : `<form>` : tag untuk membuat form.

3. Jelaskan perbedaan antara *margin* dan *padding*!<br>
    : *Margin* merupakan dua properti pada CSS yang digunakan untuk mengatur ruang di sekitar element HTML. Padding digunakan untuk mengatur ruang di sekitar konten elemen, menentukan jarak antara konten elemen serta batasannya. Sedangkan, *margin* digunakan untuk mengatur ruang di luar elemen dan digunakan untuk mengatur jarak antar satu elemen dengan elemen lainnya.

4. Jelaskan perbedaan antara *framework* CSS Tailwind dan Bootstrap! Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?<br>
    : Tailwind merupakan kerangka kerja yang dapat memberikan kendali penuh secara detail pada desain. Sedangkan, Bootstrap merupakan kerangka kerja yang menyediakan komponen-komponen tertentu, seperti navbar, kartu, dan sebagainya.
    : Sebaiknya menggunakan Bootstrap ketika ingin mengembangkan prototipe cepat dan lebih memilih pengaturan bawaan yang bagus. Sedangkan, jika kita ingin mengatur *styling* website secara lebih detail dan rinci, maka kita sebaiknya menggunakan Tailwind.

5. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step*!<br>
    : Pada tugas-tugas sebelumnya saya memang sudah menerapkan CSS pada website saya. Mulai dari warna background, warna tulisan, hingga tata letak item-item yang telah saya buat. Di sini, saya menerapkan CSS dengan menggunakan static files dari Django. Saya juga membedakan *styling* untuk setiap halamannya dengan CSS file yang berbeda. Kustomisasi ini tidak hanya pada halaman utama saja, namun pada halaman0halam lainnya seperti login, register, dan create collection.
    : Pada tugas-tugas sebelumnya, saya menggunakan tabel untuk menyajikan data yang telah dibuat. Namun, pada tugas kali ini saya mencoba untuk menyajikan data tersebut dengan pendekatan lain. Pendekatan yang saya gunakan adalah dengan menggunakan kartu. Bukan hanya kartu biasa, melainkan saya juga membuat kartu tersebut bisa membalikkan kartunya jika klik pada item tersebut dengan memberikan sedikit sentuhan JavaScript pada kartu tersebut. Pada bagian belakang kartu saya menyajikan deskripsi dari item dan tombol untuk edit dan delete. Sedangkan, pada bagian depan kartu menyajikan variabel-variabel lainnya.
    : Kemudian, untuk mengerjakan bonusnya saya juga melakukan *styling*-nya dengan CSS saja. Saya melakukannya dengan menambahkan kode berikut.
    `.collection:last-child .collection-card { color: #1062C6; }`
    : Dengan menambahkan `last-child`, kita mengidentifikasi item yang dimaksud adalah item / baris terakhir dari list itemnya.

<hr>

## Tugas 6: JavaScript dan Asynchronous JavaScript

- [x] Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
    - [x] AJAX GET
        - [x] Ubahlah kode cards data item agar dapat mendukung AJAX GET.
        - [x] Lakukan pengambilan task menggunakan AJAX GET.
    - [x] AJAX POST
        - [x] Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.
        > Modal di-trigger dengan menekan suatu tombol pada halaman utama. Saat penambahan item berhasil, modal harus ditutup dan input form harus dibersihkan dari data yang sudah dimasukkan ke dalam form sebelumnya.
        - [x]  Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.
        - [x] Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
        - [x] Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
        - [x] Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.

- [x] Melakukan perintah collectstatic.
    - Perintah ini bertujuan untuk mengumpulkan file static dari setiap aplikasi kamu ke dalam suatu folder yang dapat dengan mudah disajikan pada produksi.

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
    : Pada *asynchronus programming* tugas-tugas dapat dijalankan langsung secara bersamaan tanpa harus menunggu tugas lainnya. Sedangkan, pada *synchronus programming* tugas-tugas akan dijalankan secara sekuensial atau dengan kata lain, tugas dijalankan satu persatu dan harus menunggu tugas-tugas lainnya.
2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    : *Event-driven programming* merupakan sebuah paradigma yang akan menjalankan tugas tersebut berdasarkan peristiwa atau kejadian yang terjadi pada sistem. Paradigma ini merupakan hasil atau respon dari peristiwa yang dilakukan pada suatu program.
    : Contohnya pada tugas ini adalah ketika *user* menekan tombol `Add Product` pada modal yang telah saya tuliskan di `script-main.js`. Bahkan, di file tersebut juga terdapat beberapa contoh lain dari paradigma ini yang disebutkan secara jelas dengan adanya *syntax* `addEventListener()`.
3. Jelaskan penerapan asynchronous programming pada AJAX.
    : Dengan adanya *asynchronus programming* yang diterapkan pada AJAX, aplikasi dapat membuat request ke server. Hal ini memungkinkan AJAX dapat melanjutkan eksekusi kode JavaScript lainnya, tanpa harus menunggu respons.
    : Contoh penerapannya adalah pada `await fetch()`, `await` berfungsi untuk menunggu respons dari web. Namun, program lainnya yang ada di dalam fungsi yang sama akantetap dapat dijalankan secara bersamaan.
4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
    : Fetch API merupakan bagian dari JavaScript dan didukung oleh semua browser modern serta dapat memudahkan dalam mengelola kode yang bersifat *asynchronus*. Pada Fecth API juga memiliki sintaks yang lebih simpel dan lebih mudah dalam membacanya jika dibandingkan dengan jQuery. Sedangkan, jQuery adalah library eksternal JavaScript yang perlu diimpor. Namun, jQuery dirancang untuk dapat dijalankan di berbagai macam browser, bahkan browser yang lebih lama.
    : Menurut saya sendiri, saya lebih memilih untuk menggunakan Fetch API. Hal tersebut dikarenakan Fetch API merupakan bagian dari JavaScript modern. Hal ini juga disebabkan oleh adanya kemajuan teknologi sehingga dapat dijadikan pilihan yang tepat dalam mengembangkan web yang lebih modern. Selain itu, Fetch API juga memiliki sintaks yang lebih simpel.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    : Pertama-tama, membuat fungsi `get_collection` pada file `views.py`. Kemudian, menambahkan routing untuk fungsi tersebut pada file `urls.py`. Selanjutnya, saya memodifikasi file `script-main.js` saya agar dapat mengambil data-data dengan fungsi `getCollections()` dan menaruhnya pada cards yang telah dibuat.
    : Lalu, saya membuat tombol yang dapat membuka sebuah modal untuk menambahkan koleksi pada museum. Selanjutnya, saya membuat fungsi `add_collection_ajax` pada file `views.py` dan menambahkan routingnya pada `urls.py`. Kemudian, membuat modal pada file `main.html` dan menghubungkan form dengan fungsi `add_collection_ajax`-nya. Lalu, menambahkannya di file `script-main.js` pada fungsi `addCollection()` dengan menggunakan method `POST`. Setelah semua selesai, saya melakukan kostumisasi pada file css saya. Terakhir, saya melakukan collectstatic dengan mengetik `python3 manage.py collectstatic`.
