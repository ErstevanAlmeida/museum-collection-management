## Nama    : Erstevan Laurel Lucky Almeida
## NPM     : 2206082493
## Kelas   : PBP - E

## Tugas 2 : Implementasi MVT pada Django

Jawab:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
    Pertama-tama saya membuat proyek Django baru yang saya beri nama 'museum_collection_management'. Hal itu dapat saya lakukan dengan 'django-admin startproject museum_collection_management. Kemudian, membuat aplikasi yang bernama main dengan syntax python manage.py startapp main. Selanjutnya, melakukan routing dan membuat model dalam aplikasi main. Lalu, pada saat membuat model, saya juga membuat atribut-atribut, seperti name, type, collection, year, amount, dan description. setiap attribut memiliki tipe-nya tersendiri. Seperti contohnya, name, collection, dan type memiliki tipe CharField. Sedangkan year dan amount memiliki tipe IntegerField. Lalu, description saya membuatnya dengan tipe TextField.

    Kemudian, membuat fungsi pada views.py pada aplikasi main yang bertujuan untuk menyimpan data yang akan digunakan di web nanti. Selanjutnya melakukan routing kembali agar dapat memetakan fungsi yang telah dibuat. Langkah yang terakhir, adalah melakukan deployment dengan menggunakan Adaptable.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!
    : Client request -> urls.py -> views.py -> models.py -> Template (HMTL file) -> Response -> Client

    Pertama-tama, client akan melakukan request dengan cara membuka web browser dan mengetik url aplikasinya. Kemudia Django menerima request tersebut serta menghubungkan url yang diminta dengan views yang sesuai. Hal tersebut dapat terjadi dengan menggunakan url patterns yang sudah di-assign sebelumnya di urls.py. Selanjutnya, Django akan mengarahkan request tersebut kepada views yang sesuai yang ada pada views.py. Di dalam views.py terdapat fungsi yang digunakan untuk mengelola data.
    
    Jika fungsi yang terdapat pada views.py memerlukan data dari database, maka kita pelru mendefinisikan terlebih dahulu struktur data setiap variabel pada models.py. Selanjutnya, beralih ke HTML Template yang digunakan untuk membuat tampilan yang akan ditampilkan. HTML Template sendiri memiliki fungsi untuk memisahkan pengerjaan UI dengan fungsi-fungsi interaksi yang ada di belakang tampilannya. Terakhir, Django akan merespons dan menggabungkan HTML Template dengan data yang ada pada views.py. Respons yang dihasilkan akan dikirim kembali ke tampilan browser pengguna.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    : Virtual environement sangat berguna untuk mengisolasi proyek yang sedang dikerjakan. Hal ini dapat membuat kita menggunakan berbagai kebutuhan yang kita butuhkan untuk membangun sebuah proyek. Karena, terkadang setiap proyek yang kita kerjakan membutuhkan kebutuhan yang berbeda-beda antar proyeknya. Maka dari itu, kita membutuhkan virtual environment dalam membangun proyek ini.

    Sebenarnya, kita akan tetap bisa membuat dan membangun aplikasi web Django tanpa menggunakan virtual environment. Namun, hal tersebut tidak dianjurkan karena banyak sekali keunggulan jika kita menggunakan virtual environment. Seperti, kebersihan, keamanan, dan juga untuk menghindari konflik antar package.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya!
    : Model View-Controller (MVC) merupakan pola desain atau arsitektur perangkat lunak yang membagi aplikasi menjadi tiga komponen utama. Model merupakan komponen yang bertugas dalam pengelolaan data. View yang bertugas untuk mengatur tampilan (UI) pada sebuah perangkat lunak. 

    Model View-Template (MVT) merupakan sebuah pola yang mirip dengan MVC. Namun, pola ini paling sering digunakan pada Django. Hal yang membedakan MVT dengan MVC adalah pada komponen View. Pada MVT, komponen View tidak digunakan untuk mengatur UI. Template yang akan mengatur UI dari perangkat lunak tersebut.

    Model View-ViewModel (MVVM) merupakan sebuah pola desain untuk pengembangan perangkat lunak. Model dan View yang terdapat di MVVM ini sama saja seperti Model dan View pada MVC dan MVC. Namun, terdapat komponen baru yakni ViewModel yang digunakan untuk mengatur logika dari presentasi sebuah web agar menjadi lebih efisien.

    Salah satu perbedaannya, yakni dalam aspek implementasinya. MVC kerap kali digunakan pada desain software yang lebih umum. MVT dikerjakan pada framework Django. MVVM digunakan ketika sedang membuat desain yang lebih kompleks karena adanya VM yang dapat membuat logika presentasi menjadi lebih efisien. 

## Tugas 3: Implementasi Form dan Data Delivery pada Django

1. Apa perbedaan antara form POST dan form GET dalam Django?
    Terdapat beberapa perbedaan antar POST dan GET pada Django. Beikut adalah perbedaan-perbedaannya:
    * Method POST seringkali digunakan untuk mengirim data ke database. Sedangkan, method GET seringkali digunakan hanya untuk mengambil data.
    * Ketika sebuah data dikirim menggunakan method POST, maka data tersebut tidak akan muncul di url. Namun, jika data tersebut dikirim menggunakan method GET, maka data tersebut akan muncul di url. Hal ini berkaitan dengan keamanan data pengguna.
    * Pada method POST tidak memiliki batasan jumlah karakter yang dikirimkan. Sedangkan, pada method GET memiliki batasan jumlah karakter yang dikarenakan harus dituliskan ke url dan url memiliki batasan karakter.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    Dari segi tampilannya, 
    * XML memiliki struktur yang lebih hierarkis, namun agak sulit untuk dibaca oleh manusia.
    * JSON menampilkan data yang lebih ringan dan lebih mudah untuk dibaca oleh manusia maupun mesin. Hal tersebut dikarenakan JSON memiliki struktur berupa objek.
    * HTML seringkali digunakan oleh developer untuk membuat dan merancang tampilan dari sebuah web, seperti menentukan posisi, dan sebagainya.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    Karena JSON memiliki struktur yang lebih ringkas dan lebih mudah untuk dibaca oleh manusia. Data pada JSON juga disusun berdasarkan objeknya sehingga dapat lebih mudah untuk diidentifikasi oleh developer.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Hal pertama yang saya lakukan pastinya adalah melanjutkan proyek yang sudah saya kerjakan pada minggu sebelumnya. Kemudian, saya membuat file baru bernama `base.html` untuk membuat template file HTML yang dapat saya digunakan sebagai base untuk setiap file HTML saya. Lalu, memasukkannya pada `settings.py` dan merevisi berkas `main.html` saya. Selanjutnya, saya membuat form untuk menginput data pada berkas baru `forms.py` serta menghubungkannya denganproyek yang tengah saya buat dengan menambahkannya pada `views.py`. Pada berkas tersebut, saya membuat fungsi baru bernama `create_collection` yang akan digunakan untuk menambahkan  baru serta menambahkan syntax baru pada fungsi `show_main` (termasuk counter untuk menghitung jumlah koleksi yang ada). Hal ini akan digunakan untuk menampilkan produk tersebut.

    Setelah itu, saya menambahkan path url untuk `create_collection` pada `urls.py`. Kemudian, membuat berkas HTML baru untuk menambahkan koleksi ke database. Lalu, mengubah output pada berkas `main.html` untuk bisa mengiterasi koleksi yang ada di database. Selanjutnya, membuat sebuah function baru pada `views.py` yang bertujuan untuk mengembalikan data dalam bentuk XML. Hal yang sama juga saya lakukan untuk mengembalikan data dalam bentuk JSON, serta mengakses berdasarkan ID-nya baik pada XML, maupun JSON. Terakhir, mengakses di Postman dan melakukan push ke GitHub.

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