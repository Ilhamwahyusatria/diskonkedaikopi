<h1>▶️ Ananda Coffee</h1>
Ananda Coffee adalah sebuah program yang memungkinkan pengguna untuk memesan minuman kopi dan mendapatkan diskon berdasarkan jumlah pesanan yang dilakukan. Program ini ditulis dalam bahasa Python dan memiliki fitur-fitur sebagai berikut:

• Menampilkan daftar menu minuman kopi beserta harga.
• Memungkinkan pengguna untuk memilih menu dan menginput jumlah pesanan.
• Menghitung total harga pesanan, termasuk diskon dan PPN.
• Menampilkan rincian pesanan beserta total harga yang harus dibayar.
• Memungkinkan pengguna untuk memesan kembali.

<h1>▶️ Cara Menggunakan Program</h1>
Untuk menggunakan program Ananda Coffee, lakukan langkah-langkah sebagai berikut:

1. Pastikan Python sudah terinstall di komputer Anda.
2. Unduh atau salin kode program Ananda Coffee.
3. Jalankan program dengan perintah python ananda_coffee.py.
4. Program akan menampilkan daftar menu kopi dan meminta pengguna untuk memilih menu dan menginput jumlah pesanan.
5. Program akan menghitung total harga pesanan beserta diskon dan PPN, dan menampilkan rincian pesanan serta total harga yang harus dibayar.
6. Pengguna dapat memilih untuk memesan kembali atau tidak dengan mengetik "Y" atau "N".
7. Jika pengguna memilih untuk memesan kembali, program akan kembali ke langkah 4.

<h1>▶️ Struktur Kode Program</h1>
Program Ananda Coffee terdiri dari dua kelas utama yaitu AnandaCoffee dan Diskon. Kelas AnandaCoffee memiliki tiga metode yaitu __init__, pesan, dan __output_pesan. Metode __init__ digunakan untuk menginisialisasi daftar menu minuman kopi dan pilihan pengguna, sedangkan metode pesan digunakan untuk meng-handle input dan output pesanan serta diskon. Metode __output_pesan digunakan untuk menampilkan rincian pesanan dan total harga yang harus dibayar.

Kelas Diskon digunakan untuk menghitung diskon berdasarkan jumlah pesanan yang dilakukan oleh pengguna. Kelas Diskon memiliki lima metode yaitu __init__, diskon_1, diskon_2, diskon_3, diskon_4, dan diskon_5. Setiap metode digunakan untuk menghitung diskon berdasarkan jumlah pesanan yang berbeda-beda. Metode __init__ digunakan untuk menginisialisasi daftar diskon, sedangkan metode diskon_1 sampai diskon_5 digunakan untuk menghitung diskon berdasarkan jumlah pesanan yang dilakukan oleh pengguna.
