# Fungsi untuk mengkonversi huruf mutu menjadi angka mutu
def konversi_huruf_ke_angka(regita_huruf):
    if regita_huruf == 'A':
        return 4
    elif regita_huruf == 'AB':
        return 3.5
    elif regita_huruf == 'B':
        return 3
    elif regita_huruf == 'BC':
        return 2.5
    elif regita_huruf == 'C':
        return 2
    elif regita_huruf == 'D':
        return 1
    elif regita_huruf == 'E':
        return 0
    else:
        return None  # Jika input tidak valid

# Fungsi untuk menghitung IPS
def hitung_ips(regita_angka_mutu):
 regita_SKS = [2, 2, 2, 3, 4, 3, 4]  # SKS masing-masing mata kuliah
 regita_total_sks = sum(regita_SKS)
 regita_total_nilai = sum([a * b for a, b in zip( regita_angka_mutu, regita_SKS)])
 return regita_total_nilai / regita_total_sks #salah pada pemanggilan variabel, awalnya total_nilai / total_sks


# Fungsi untuk menentukan status kelulusan
def tentukan_status_kelulusan(regita_IPS):
    if IPS >= 2.75:
        return "Tetap"
    elif 2.00 < IPS < 2.75:
        return "Percobaan"
    elif IPS <= 2.00:
        return "Tidak Lulus"

# Input data mahasiswa
nama_mahasiswa = input("Masukkan Nama Mahasiswa: ")
NIM_mahasiswa = input("Masukkan NIM Mahasiswa: ")

# Input huruf mutu untuk setiap mata kuliah
huruf_mutu_agama = input("Masukkan Huruf Mutu Pendidikan Agama: ")
huruf_mutu_pancasila = input("Masukkan Huruf Mutu Pendidikan Pancasila: ")
huruf_mutu_inggris = input("Masukkan Huruf Mutu Bahasa Inggris 1: ")
huruf_mutu_pdi = input("Masukkan Huruf Mutu Pengolahan Data dan Informasi: ")
huruf_mutu_ptik = input("Masukkan Huruf Mutu Pengantar TI dan Komunikasi: ")
huruf_mutu_diskrit = input("Masukkan Huruf Mutu Matematika Diskrit: ")
huruf_mutu_pemrograman = input("Masukkan Huruf Mutu Pemrograman Dasar: ")

# Konversi huruf mutu ke angka mutu
angka_mutu = [
    konversi_huruf_ke_angka(huruf_mutu_agama),
    konversi_huruf_ke_angka(huruf_mutu_pancasila),
    konversi_huruf_ke_angka(huruf_mutu_inggris),
    konversi_huruf_ke_angka(huruf_mutu_pdi),
    konversi_huruf_ke_angka(huruf_mutu_ptik),
    konversi_huruf_ke_angka(huruf_mutu_diskrit),
    konversi_huruf_ke_angka(huruf_mutu_pemrograman)
]

# Hitung IPS
IPS = hitung_ips(angka_mutu)

# Tentukan status kelulusan
status_kelulusan = tentukan_status_kelulusan(IPS)

# Tampilkan hasil
print("\n===========================")
print(f"Nama Mahasiswa: {nama_mahasiswa}")
print(f"NIM Mahasiswa: {NIM_mahasiswa}")
print(f"IPS: {IPS:.2f}")
print(f"Status Kelulusan: {status_kelulusan}")
print("===========================")