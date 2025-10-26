# SISTEM-PENGELOLAHAN-SEWA-KOST 

Nama Anggota Kelompok:

Muhammad Islami Pasya (2509116108)

Muhammad Aulia Rahman (2509116096)

Muhammad Syafaat Arake (2509116090)


# Deskripsi Singkat Program Sistem Pengelolaan Sewa Kost

Program sistem pengelolaan sewa kost merupakan sebuah Sistem Manajemen Hunian Kost yang dirancang untuk mengelola berbagai aspek operasional kost secara terintegrasi melalui sistem pengelolaan berbasis digital. Program ini bertujuan menyediakan platform yang mencakup manajemen pengguna, data kamar, data penyewa, transaksi pembayaran sewa, serta pengelolaan fasilitas kost.

Alur algoritma program dimulai dengan sistem verifikasi data, di mana pengguna dapat melakukan registrasi akun baru atau login menggunakan username dan password yang sudah terdaftar. Sistem membedakan akses berdasarkan peran pengguna, yaitu admin dan penyewa. Admin memiliki kendali penuh untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada data kamar, data penyewa, serta mengelola transaksi sewa. Sementara itu, penyewa dapat melihat daftar kamar yang tersedia, melakukan pemesanan kamar, mengecek status sewa, serta melakukan pembayaran biaya kost.

Sistem ini dilengkapi dengan mekanisme validasi input yang ketat untuk menjaga integritas data, termasuk pengecekan panjang input, tipe data yang sesuai, dan penanganan terhadap interupsi keyboard. Pada sisi administrasi, program mengimplementasikan manajemen data persisten melalui penyimpanan file CSV, sehingga data pengguna, kamar, dan transaksi akan tetap tersimpan meskipun program ditutup.

Untuk meningkatkan pengelolaan sewa kost, program memanfaatkan modul PrettyTable untuk menampilkan data dalam format tabel yang rapi dan mudah dibaca. Sistem transaksi dalam program ini mengintegrasikan mekanisme pembayaran sewa yang terhubung dengan saldo pengguna, memungkinkan penyewa melakukan top-up sebelum menyelesaikan pembayaran.

Algoritma pembayaran dirancang untuk memverifikasi kecukupan saldo sebelum transaksi diproses, serta dilengkapi dengan pembuatan nota pembayaran otomatis sebagai bukti transaksi. Selain itu, admin juga dapat memantau status kamar (tersedia, dipesan, atau disewa) secara real-time. Secara keseluruhan, program ini menunjukkan implementasi algoritma yang terstruktur dan efisien dalam mengelola sistem penyewaan kost modern dengan tetap menjaga kemudahan penggunaan, akurasi data, dan keamanan transaksi.

# 1. Flowchart Menu Utama 
<img width="1811" height="1692" alt="Menu Utama PA  drawio" src="https://github.com/user-attachments/assets/c8d67e7f-8420-4490-89f0-c0026cc6d1f3" />

# 2. Flowchart Menu Admin
<img width="1852" height="2192" alt="Menu admin PA drawio" src="https://github.com/user-attachments/assets/b0dd6af8-44d6-4c58-a8d3-47bbd8a7d1bf" />

# 3. Flowchart Menu User
<img width="1831" height="1621" alt="Menu User PA drawio" src="https://github.com/user-attachments/assets/3ac26e16-7fe2-4943-bfc9-433edf5d9195" />

# Menu Utama
![Gambar WhatsApp 2025-10-26 pukul 18 19 50_c41755da](https://github.com/user-attachments/assets/97b58ae2-7747-4a9d-b8e5-510bd3d87f7c)

# Menu ini merupakan tampilan awal program yang memberikan pilihan utama kepada pengguna: masuk, registrasi, atau keluar dari sistem

# Menu Admin
![Gambar WhatsApp 2025-10-26 pukul 18 19 51_8a6df95f](https://github.com/user-attachments/assets/e9bf3e48-9da5-496b-ad8b-16648aa061a4)
# Menu ini berisi daftar pilihan untuk mengelola data kamar dan riwayat sewa. Admin dapat Melihat Daftar Kamar, Menambah Kamar baru, Mengubah (Update) detail kamar yang sudah ada, atau Menghapus Kamar. Selain itu, tersedia fungsi untuk melihat Semua Riwayat Sewa dan Mengubah Status Sewa kamar. Setelah selesai, admin dapat memilih Logout untuk keluar dari sesi atau memilih Keluar dari Program untuk menutup aplikasi

# Menu 1 Admin Lihat Daftar Kamar
![Gambar WhatsApp 2025-10-26 pukul 18 19 51_2e78be91](https://github.com/user-attachments/assets/455c3c91-2d7e-4b8f-ae21-999aa790ac68)
#  Menu ini berfungsi untuk menampilkan seluruh data kamar kos yang tersimpan di dalam sistem. Setelah menu 1 dipilih, sistem akan menampilkan sebuah tabel yang berisi informasi rinci dari setiap kamar, seperti: ID Kamar, Tipe kamar, Harga sewa, dan Status ketersediaan kamar (Tersedia atau Tidak Tersedia).

# Menu 2 Admin Tambah Kamar
![Gambar WhatsApp 2025-10-26 pukul 18 19 52_9fa4161f](https://github.com/user-attachments/assets/cc3bad4c-99c3-4258-9b15-fbadd507b184)
# Menu ini digunakan oleh admini untuk memasukkan data kamar kos yang baru ke dalam sistem pengelolaan. Setelah memilih menu ini, sistem akan meminta admin untuk mengisi detail-detail kamar baru tersebut.

# Menu 3 Admin Update Kamar
![Gambar WhatsApp 2025-10-26 pukul 18 19 52_21657e8d](https://github.com/user-attachments/assets/9778b51b-3d6c-4fbc-9520-c795c901217c)

# Menu ini berfungsi untuk mengubah atau memperbarui informasi dari kamar kos yang sudah terdaftar di dalam sistem. Admin akan menggunakan menu ini ketika ada perubahan pada detail kamar

# Menu 4 Hapus Kamar
![Gambar WhatsApp 2025-10-26 pukul 18 19 53_49587fec](https://github.com/user-attachments/assets/17f7ea83-c886-436b-875a-101451ab7d0e)

# Menu ini berfungsi untuk menghilangkan atau menghapus data kamar kos tertentu secara permanen dari sistem pengelolaan.

# Menu 5 Lihat Semua Riwayat Sewa
![Gambar WhatsApp 2025-10-26 pukul 18 19 54_dfff11d9](https://github.com/user-attachments/assets/7b2ce307-97fd-4dee-85cd-053936183cba)
#  Menu ini berfungsi untuk menampilkan catatan lengkap dari seluruh transaksi penyewaan kamar kos yang udah disewa.

# Menu 6 Admin Mengubah Status Sewa
![Gambar WhatsApp 2025-10-26 pukul 18 19 54_71eab0d1](https://github.com/user-attachments/assets/37c3d0f6-fa59-4e2e-bd5d-47533df0361e)

# Menu ini berfungsi untuk mengelola dan memperbarui kondisi atau status dari transaksi penyewaan kamar yang sedang berjalan.

# Menu 9 Logout
<img width="490" height="336" alt="Screenshot 2025-10-25 215533" src="https://github.com/user-attachments/assets/e95770b6-2f85-4054-be92-9f4d95925987" />

# Menu kesembilan ini untuk logout dari menu, lalu bisa masuk ke menu user

# Menu User
![Gambar WhatsApp 2025-10-26 pukul 18 46 25_9ed1e2d0](https://github.com/user-attachments/assets/83d49210-7187-4baf-8894-ff354bae6dc0)

#  Menu ini berfungsi sebagai pusat layanan bagi penyewa kos, memungkinkan mereka untuk melihat kamar yang tersedia, melakukan sewa kamar, meninjau riwayat sewa pribadi, serta mengelola keuangan melalui fitur cek dan isi saldo sebelum melakukan logout atau menutup program.

# Menu 1 User Lihat Kamar Tersedia
![Gambar WhatsApp 2025-10-26 pukul 18 46 26_db30a88d](https://github.com/user-attachments/assets/2ff28540-c771-4c5b-8e60-7394cbf5836a)

#  Menu ini berfungsi untuk menampilkan daftar kamar kos yang statusnya sedang Tersedia (kosong) dan siap untuk disewa oleh penyewa.

# Menu 2 User Sewa Kamar
![Gambar WhatsApp 2025-10-26 pukul 18 46 26_9f956a92](https://github.com/user-attachments/assets/792eb4ff-cdc9-4624-b55c-36a75dffe27e)

# Menu ini memungkinkan penyewa untuk melakukan proses pemesanan dan pembayaran sewa untuk kamar yang telah mereka pilih dari daftar kamar yang tersedia.

# Menu 3 User Melihat Riwayat Sewa
![Gambar WhatsApp 2025-10-26 pukul 18 46 27_b99f34c6](https://github.com/user-attachments/assets/cef24c40-eb63-46e8-aff8-7d480fd189a1)

#  Menu ini berfungsi untuk menampilkan catatan semua transaksi penyewaan yang telah dilakukan oleh pengguna yang sedang login.


# Menu 4 User Cek Saldo
![Gambar WhatsApp 2025-10-26 pukul 18 46 27_d3b78349](https://github.com/user-attachments/assets/a8fc8966-f378-4f59-bcf4-f2b2a3300dff)

#  Menu ini berfungsi untuk menampilkan jumlah dana atau uang yang saat ini tersimpan di dalam akun pengguna (penyewa) di sistem tersebut.

# Menu 5 User Isi Saldo
![Gambar WhatsApp 2025-10-26 pukul 18 46 28_24178536](https://github.com/user-attachments/assets/aca2ff6d-6b9c-45dc-ad5a-7c3192cabe69)

#  Menu ini berfungsi untuk melakukan pengisian dana atau penambahan uang ke saldo akun pengguna (penyewa) yang ada di dalam sistem.

# Menu 1 dari menu utama
<img width="435" height="176" alt="Screenshot 2025-10-26 030110" src="https://github.com/user-attachments/assets/e23c8bcd-a637-42a8-8096-1b524d8d19ad" />

# Menu ini berfungsi untuk memverifikasi dan mengautentikasi pengguna yang sudah memiliki akun agar bisa masuk ke sistem sesuai dengan perannya (admin atau penyewa).Menu ini berfungsi sebagai gerbang masuk ke sistem yang memastikan hanya pengguna terdaftar yang dapat mengakses fitur-fitur program sesuai hak aksesnya, sehingga mendukung keamanan dan pengelolaan data kost yang teratur

# Menu 2 dari menu utama
<img width="757" height="393" alt="Screenshot 2025-10-25 220600" src="https://github.com/user-attachments/assets/2fa0ed5c-fcfe-4dfe-a4c5-74cd72379a52" />

# Menu 2 berfungsi untuk menambahkan akun penyewa baru ke dalam sistem, agar pengguna dapat login dan mulai menggunakan fitur-fitur dalam program pengelolaan kost seperti melihat kamar, melakukan pemesanan, dan pembayaran sewa.

# Menu 0 dari menu utama 
<img width="598" height="197" alt="Screenshot 2025-10-25 220618" src="https://github.com/user-attachments/assets/2531dfc7-411d-4159-9268-fb5502341a62" />

# Menu Merupakan akhir dari program jika menginputkan 0, pilihan ini adalah satu nya untuk keluar dari program tersebut.











