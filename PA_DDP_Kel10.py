import csv
import os
from prettytable import PrettyTable
import pwinput
from datetime import datetime

users_file = "users.csv"
kost_file = "kost.csv"
registrasi_file = "registrasi.csv"

SALDO_MAX = 1_000_000_000
DEPOSIT_MIN = 100_000
HARGA_MIN = 100_000
HARGA_MAX = 10_000_000
DURASI_MAX_BULAN = 60

def is_valid_name(text):
    if not text or len(text.strip()) < 2:
        return False
    for char in text:
        if not (char.isalpha() or char.isspace()):
            return False
    return True

def is_valid_address(text):
    if not text or len(text.strip()) < 3:
        return False
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.-"
    for char in text:
        if char not in allowed:
            return False
    return True

def is_valid_username(text):
    if not text or len(text) < 3:
        return False
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
    for char in text:
        if char not in allowed:
            return False
    return True

def is_not_empty(text):
    return bool(text.strip())

def initialize_data():
    if not os.path.exists(users_file):
        with open(users_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "password", "role", "nama", "alamat", "no_hp", "saldo"])
            writer.writerow(["admin", "admin123", "admin", "Admin Kost", "-", "-", "0"])

    if not os.path.exists(kost_file):
        with open(kost_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id_kamar", "tipe_kamar", "harga", "status"])

    if not os.path.exists(registrasi_file):
        with open(registrasi_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["tanggal", "username", "nama_penyewa", "id_kamar", "tipe_kamar", "harga", "durasi", "status"])

def load_data():
    users = {}
    kamar = {}
    registrasi = []

    if os.path.exists(users_file):
        with open(users_file, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                users[row["username"]] = {
                    "password": row["password"],
                    "role": row["role"],
                    "nama": row["nama"],
                    "alamat": row["alamat"],
                    "no_hp": row["no_hp"],
                    "saldo": int(row["saldo"])
                }

    if os.path.exists(kost_file):
        with open(kost_file, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                kamar[row["id_kamar"]] = {
                    "tipe_kamar": row["tipe_kamar"],
                    "harga": int(row["harga"]),
                    "status": row["status"]
                }

    if os.path.exists(registrasi_file):
        with open(registrasi_file, "r", newline="") as f:
            reader = csv.DictReader(f)
            registrasi = [row for row in reader]

    return users, kamar, registrasi

def save_data(users, kamar, registrasi):
    with open(users_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["username", "password", "role", "nama", "alamat", "no_hp", "saldo"])
        for username, data in users.items():
            writer.writerow([username, data["password"], data["role"], data["nama"], data["alamat"], data["no_hp"], data["saldo"]])

    with open(kost_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id_kamar", "tipe_kamar", "harga", "status"])
        for id_kamar, data in kamar.items():
            writer.writerow([id_kamar, data["tipe_kamar"], data["harga"], data["status"]])

    with open(registrasi_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["tanggal", "username", "nama_penyewa", "id_kamar", "tipe_kamar", "harga", "durasi", "status"])
        for r in registrasi:
            writer.writerow(r.values())

def login(users):
    try:
        print("\n=== Login ===")
        username = input("Username: ")
        password = pwinput.pwinput("Password: ")

        if username in users and users[username]["password"] == password:
            print(f"Selamat datang, {username} ({users[username]['role']})!")
            return username
        else:
            print("Username atau password salah")
            return None
    except KeyboardInterrupt:
        print("jangan ctrl C Ganteng")
        login(users)

def register(users, kamar, registrasi):
    print("\n=== Registrasi Penyewa Baru ===")
    print("(Ketik '0' untuk membatalkan registrasi dan kembali ke menu utama)")

    while True:
        username = input("Username: ").strip()
        if username == "0":
            return
        if not is_not_empty(username):
            print("Username tidak boleh kosong.")
        elif not is_valid_username(username):
            print("Username hanya boleh huruf, angka, underscore (_), atau dash (-), minimal 3 karakter.")
        elif username in users:
            print("Username sudah terdaftar.")
        else:
            break

    while True:
        password = pwinput.pwinput("Password: ")
        if password == "0":
            return
        if not is_not_empty(password):
            print("Password tidak boleh kosong.")
        elif len(password) < 6:
            print("Password minimal 6 karakter.")
        else:
            break

    while True:
        nama = input("Nama Lengkap: ").strip()
        if nama == "0":
            return
        if not is_not_empty(nama):
            print("Nama tidak boleh kosong.")
        elif not is_valid_name(nama):
            print("Nama hanya boleh huruf dan spasi, minimal 2 karakter.")
        else:
            break

    while True:
        alamat = input("Alamat: ").strip()
        if alamat == "0":
            return
        if not is_not_empty(alamat):
            print("Alamat tidak boleh kosong.")
        elif not is_valid_address(alamat):
            print("Alamat hanya boleh huruf, angka, spasi, koma, titik, atau strip.")
        else:
            break

    while True:
        no_hp = input("No. HP (hanya angka, min 10 digit): ").strip()
        if no_hp == "0":
            return
        if not is_not_empty(no_hp):
            print("No. HP tidak boleh kosong.")
        elif not no_hp.isdigit():
            print("No. HP hanya boleh angka.")
        elif len(no_hp) < 10:
            print("No. HP minimal 10 digit.")
        else:
            break

    users[username] = {
        "password": password,
        "role": "penyewa",
        "nama": nama,
        "alamat": alamat,
        "no_hp": no_hp,
        "saldo": 0
    }
    save_data(users, kamar, registrasi)
    print("Registrasi berhasil!")

def display_kamar(kamar):
    if not kamar:
        print("\nBelum ada kamar tersedia.")
        return
    table = PrettyTable()
    table.field_names = ["ID Kamar", "Tipe", "Harga (Rp)", "Status"]
    for id_kamar, data in kamar.items():
        table.add_row([id_kamar, data["tipe_kamar"], f"Rp {data['harga']:,}", data["status"]])
    print("\n=== Daftar Kamar Kost ===")
    print(table)

def tambah_kamar(users, kamar, registrasi):
    print("\n=== Tambah Kamar Baru ===")
    print("Ketik '0' kapan saja untuk kembali ke menu admin.")

    while True:
        tipe_input = input("Nama tipe kamar: ").strip()
        if tipe_input == "0":
            return
        if not tipe_input:
            print("Nama tipe tidak boleh kosong.")
            continue
        tipe = f"Kamar {tipe_input}"
        break

    while True:
        harga_input = input(f"Harga per bulan (Rp{HARGA_MIN:,} - Rp{HARGA_MAX:,}): ").strip()
        if harga_input == "0":
            return

        try:
            harga = int(harga_input)
            if harga < HARGA_MIN:
                print(f"Harga minimal Rp{HARGA_MIN:,}.")
            elif harga > HARGA_MAX:
                print(f"Harga maksimal Rp{HARGA_MAX:,}.")
            else:
                break
        except ValueError:
            print("Input harga tidak valid. Masukkan angka.")

    print(f"\nKonfirmasi Penambahan:")
    print(f"Tipe: {tipe}")
    print(f"Harga: Rp {harga:,}")
    print("1. Simpan")
    print("0. Kembali")

    while True:
        pilih = input("Pilih: ").strip()
        if pilih == "1":
            id_kamar = str(max(map(int, kamar.keys())) + 1) if kamar else "1"
            kamar[id_kamar] = {"tipe_kamar": tipe, "harga": harga, "status": "Tersedia"}
            save_data(users, kamar, registrasi)
            print(f"Kamar berhasil ditambahkan! ID: {id_kamar}")
            return
        elif pilih == "0":
            return
        else:
            print("Pilihan tidak valid. Ketik 1 atau 0.")

def update_kamar(users, kamar, registrasi):
    while True:
        display_kamar(kamar)
        id_kamar = input("ID kamar yang akan diedit (ketik '0' untuk batal): ").strip()
        if id_kamar == "0":
            return
        if id_kamar not in kamar:
            print("Kamar tidak ditemukan. Silakan coba lagi.")
            continue

        tipe = input("Tipe baru (Enter untuk tidak mengubah): ").strip()
        harga = input("Harga baru (Enter untuk tidak mengubah): ").strip()
        status = input("Status baru (Tersedia/Tidak Tersedia, Enter untuk tidak mengubah): ").strip()

        updated = False

        if tipe:
            kamar[id_kamar]["tipe_kamar"] = f"Kamar {tipe}" if not tipe.startswith("Kamar ") else tipe
            updated = True

        if harga:
            try:
                harga = int(harga)
                if HARGA_MIN <= harga <= HARGA_MAX:
                    kamar[id_kamar]["harga"] = harga
                    updated = True
                else:
                    print(f"Harga harus antara Rp{HARGA_MIN:,} dan Rp{HARGA_MAX:,}.")
            except ValueError:
                print("Harga harus berupa angka.")

        if status in ["Tersedia", "Tidak Tersedia"]:
            kamar[id_kamar]["status"] = status
            updated = True
        elif status:
            print("Status hanya boleh 'Tersedia' atau 'Tidak Tersedia'.")

        if updated:
            save_data(users, kamar, registrasi)
            print("Kamar berhasil diperbarui.")
        else:
            print("Tidak ada perubahan yang disimpan.")
        return

def hapus_kamar(users, kamar, registrasi):
    while True:
        display_kamar(kamar)
        id_kamar = input("ID kamar yang akan dihapus (ketik '0' untuk batal): ").strip()
        if id_kamar == "0":
            return
        if id_kamar not in kamar:
            print("Kamar tidak ditemukan. Silakan coba lagi.")
            continue

        konfirmasi = input(f"Yakin ingin menghapus kamar {id_kamar}? (y/n): ").strip().lower()
        if konfirmasi == 'y':
            del kamar[id_kamar]
            save_data(users, kamar, registrasi)
            print("Kamar berhasil dihapus.")
            return
        else:
            print("Penghapusan dibatalkan.")
            return

def lihat_riwayat(username, registrasi, is_admin=False):
    table = PrettyTable()
    table.field_names = ["Tanggal", "Nama", "Kamar", "Durasi (bln)", "Harga", "Status"]
    data = registrasi if is_admin else [r for r in registrasi if r["username"] == username]
    if not data:
        print("Belum ada riwayat sewa.")
        return
    for r in data:
        table.add_row([r["tanggal"], r["nama_penyewa"], r["tipe_kamar"], r["durasi"], f"Rp {int(r['harga']):,}", r["status"]])
    print("\n=== Riwayat Sewa ===")
    print(table)

def ubah_status_sewa(users, kamar, registrasi):
    while True:
        lihat_riwayat(None, registrasi, True)
        nama = input("Nama penyewa (ketik '0' untuk batal): ").strip()
        if nama == "0":
            return

        found = None
        for r in registrasi:
            if r["nama_penyewa"].lower() == nama.lower():
                found = r
                break

        if not found:
            print("Penyewa tidak ditemukan. Silakan coba lagi.")
            continue

        status = input("Status baru (Aktif/Selesai/Dibatalkan): ").strip()
        if status not in ["Aktif", "Selesai", "Dibatalkan"]:
            print("Status tidak valid. Harus salah satu dari: Aktif, Selesai, Dibatalkan.")
            continue

        found["status"] = status
        save_data(users, kamar, registrasi)
        print("Status sewa berhasil diubah.")
        return

def sewa_kamar(username, users, kamar, registrasi):
    display_kamar(kamar)
    while True:
        id_kamar = input("ID kamar yang ingin disewa (ketik '0' untuk batal): ").strip()
        if id_kamar == "0":
            return
        if id_kamar not in kamar:
            print("Kamar tidak ditemukan. Silakan coba lagi.")
            display_kamar(kamar)
            continue
        if kamar[id_kamar]["status"] != "Tersedia":
            print("Kamar tidak tersedia. Silakan pilih kamar lain.")
            display_kamar(kamar)
            continue
        break

    while True:
        durasi_input = input(f"Durasi sewa (1-{DURASI_MAX_BULAN} bulan, ketik '0' untuk batal): ").strip()
        if durasi_input == "0":
            return
        try:
            durasi = int(durasi_input)
            if durasi < 1:
                print("Durasi minimal 1 bulan.")
            elif durasi > DURASI_MAX_BULAN:
                print(f"Maksimal durasi: {DURASI_MAX_BULAN} bulan.")
            else:
                break
        except ValueError:
            print("Masukkan angka yang valid.")

    total = kamar[id_kamar]["harga"] * durasi
    while True:
        konfirmasi = input(f"Total: Rp {total:,}. Konfirmasi? (y/n/0 untuk batal): ").strip()
        if konfirmasi == "0":
            return
        elif konfirmasi.lower() == 'y':
            record = {
                "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "username": username,
                "nama_penyewa": users[username]["nama"],
                "id_kamar": id_kamar,
                "tipe_kamar": kamar[id_kamar]["tipe_kamar"],
                "harga": kamar[id_kamar]["harga"],
                "durasi": str(durasi),
                "status": "Aktif"
            }
            registrasi.append(record)
            kamar[id_kamar]["status"] = "Tidak Tersedia"
            save_data(users, kamar, registrasi)
            print("Sewa berhasil!")
            return
        elif konfirmasi.lower() == 'n':
            print("Sewa dibatalkan.")
            return
        else:
            print("Pilihan tidak valid. Masukkan y, n, atau 0.")

def cek_saldo(username, users):
    print(f"\nSaldo Anda: Rp {users[username]['saldo']:,}")

def isi_saldo(username, users, kamar, registrasi):
    while True:
        jumlah_input = input(f"\nJumlah deposit (min Rp{DEPOSIT_MIN:,}, ketik '0' untuk batal): Rp ").strip()
        if jumlah_input == "0":
            return
        try:
            jumlah = int(jumlah_input)
            if jumlah < DEPOSIT_MIN:
                print(f"Minimal deposit: Rp{DEPOSIT_MIN:,}.")
            elif users[username]["saldo"] + jumlah > SALDO_MAX:
                print(f"Saldo maksimal: Rp{SALDO_MAX:,}.")
            else:
                users[username]["saldo"] += jumlah
                save_data(users, kamar, registrasi)
                print(f"Saldo sekarang: Rp {users[username]['saldo']:,}")
                return
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

def admin_menu(users, kamar, registrasi, username):
    try:
        while True:
            print("\n=== Menu Admin Kost ===")
            print("1. Lihat Daftar Kamar")
            print("2. Tambah Kamar")
            print("3. Update Kamar")
            print("4. Hapus Kamar")
            print("5. Lihat Semua Riwayat Sewa")
            print("6. Ubah Status Sewa")
            print("9. Logout")
            print("0. Keluar dari Program")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                display_kamar(kamar)
            elif pilihan == "2":
                tambah_kamar(users, kamar, registrasi)
            elif pilihan == "3":
                update_kamar(users, kamar, registrasi)
            elif pilihan == "4":
                hapus_kamar(users, kamar, registrasi)
            elif pilihan == "5":
                lihat_riwayat(username, registrasi, True)
            elif pilihan == "6":
                ubah_status_sewa(users, kamar, registrasi)
            elif pilihan == "9":
                print("Anda telah logout.")
                return
            elif pilihan == "0":
                print("Terima kasih! Sampai jumpa.")
                exit()
            else:
                print("Pilihan tidak valid.")
    except KeyboardInterrupt:
        print("\n Jangan ctrl c ganteng")
        admin_menu(users, kamar, registrasi, username)
    except EOFError:
        print("\n Jangan ctrl z ganteng")

def penyewa_menu(users, kamar, registrasi, username):
    try:
        while True:
            print("\n=== Menu Penyewa Kost ===")
            print("1. Lihat Kamar Tersedia")
            print("2. Sewa Kamar")
            print("3. Lihat Riwayat Sewa")
            print("4. Cek Saldo")
            print("5. Isi Saldo")
            print("9. Logout")
            print("0. Keluar dari Program")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                display_kamar(kamar)
            elif pilihan == "2":
                sewa_kamar(username, users, kamar, registrasi)
            elif pilihan == "3":
                lihat_riwayat(username, registrasi)
            elif pilihan == "4":
                cek_saldo(username, users)
            elif pilihan == "5":
                isi_saldo(username, users, kamar, registrasi)
            elif pilihan == "9":
                print("Anda telah logout.")
                return
            elif pilihan == "0":
                print("Terima kasih! Sampai jumpa.")
                exit()
            else:
                print("Pilihan tidak valid.")
    except KeyboardInterrupt:
        print("\n Jangan ctrl c ganteng")
    except EOFError:
        print("\n Jangan ctrl z ganteng")

def main():
    try:
        initialize_data()
        users, kamar, registrasi = load_data()

        while True:
            print("\n=== Sistem Pengelolaan Sewa Kost ===")
            print("1. Login")
            print("2. Registrasi")
            print("0. Keluar dari Program")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                username = login(users)
                if username:
                    if users[username]["role"] == "admin":
                        admin_menu(users, kamar, registrasi, username)
                    else:
                        penyewa_menu(users, kamar, registrasi, username)
            elif pilihan == "2":
                register(users, kamar, registrasi)
            elif pilihan == "0":
                print("Terima kasih telah menggunakan layanan kami!")
                break
            else:
                print("Pilihan tidak tersedia.")
    except KeyboardInterrupt:
        print("\n Jangan ctrl c ganteng")
        main()
    except EOFError:
        print("\n Jangan ctrl z ganteng")
        main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("keluar")



