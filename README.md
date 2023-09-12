Nama    : Erstevan Laurel Lucky Almeida

NPM     : 2206082493

Kelas   : PBP - E

Tugas 2 : Implementasi MVT pada Django

Jawab:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
    : Pertama-tama saya membuat proyek Django baru yang saya beri nama 'museum_collection_management'. Hal itu dapat saya lakukan dengan 'django-admin startproject museum_collection_management. Kemudian, membuat aplikasi yang bernama main dengan syntax python manage.py startapp main. Selanjutnya, melakukan routing dan membuat model dalam aplikasi main. Lalu, pada saat membuat model, saya juga membuat atribut-atribut, seperti name, type, collection, year, amount, dan description. setiap attribut memiliki tipe-nya tersendiri. Seperti contohnya, name, collection, dan type memiliki tipe CharField. Sedangkan year dan amount memiliki tipe IntegerField. Lalu, description saya membuatnya dengan tipe TextField.

    Kemudian, membuat fungsi pada views.py pada aplikasi main yang bertujuan untuk menyimpan data yang akan digunakan di web nanti. Selanjutnya melakukan routing kembali agar dapat memetakan fungsi yang telah dibuat. Langkah yang terakhir, adalah melakukan deployment dengan menggunakan Adaptable.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    : Virtual environement sangat berguna untuk mengisolasi proyek yang sedang dikerjakan. Hal ini dapat membuat kita menggunakan berbagai kebutuhan yang kita butuhkan untuk membangun sebuah proyek. Karena, terkadang setiap proyek yang kita kerjakan membutuhkan kebutuhan yang berbeda-beda antar proyeknya. Maka dari itu, kita membutuhkan virtual environment dalam membangun proyek ini.

    Sebenarnya, kita akan tetap bisa membuat dan membangun aplikasi web Django tanpa menggunakan virtual environment. Namun, hal tersebut tidak dianjurkan karena banyak sekali keunggulan jika kita menggunakan virtual environment. Seperti, kebersihan, keamanan, dan juga untuk menghindari konflik antar package.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya!
    : Model View-Controller (MVC) merupakan pola desain atau arsitektur perangkat lunak yang membagi aplikasi menjadi tiga komponen utama. Model merupakan komponen yang bertugas dalam pengelolaan data. View yang bertugas untuk mengatur tampilan (UI) pada sebuah perangkat lunak. 

    Model View-Template (MVT) merupakan sebuah pola yang mirip dengan MVC. Namun, pola ini paling sering digunakan pada Django. Hal yang membedakan MVT dengan MVC adalah pada komponen View. Pada MVT, komponen View tidak digunakan untuk mengatur UI. Template yang akan mengatur UI dari perangkat lunak tersebut.

    Model View-ViewModel (MVVM) merupakan sebuah pola desain untuk pengembangan perangkat lunak. Model dan View yang terdapat di MVVM ini sama saja seperti Model dan View pada MVC dan MVC. Namun, terdapat komponen baru yakni ViewModel yang digunakan untuk mengatur logika dari presentasi sebuah web agar menjadi lebih efisien.

    Salah satu perbedaannya, yakni dalam aspek implementasinya. MVC kerap kali digunakan pada desain software yang lebih umum. MVT dikerjakan pada framework Django. MVVM digunakan ketika sedang membuat desain yang lebih kompleks karena adanya VM yang dapat membuat logika presentasi menjadi lebih efisien. 
