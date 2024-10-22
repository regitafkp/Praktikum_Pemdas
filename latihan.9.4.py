# Memasukan variabel
regita_nama = "Regita"
regita_umur = 18
regita_program_studi = "Sistem Informasi"
regita_jenis_kelamin = "Perempuan"
regita_tinggi = 163
regita_kelas = "SI-1A"
regita_lulus = False

# Mengubah nilai variabel
regita_nama = "Regita"
regita_umur = 18
regita_tinggi = 163
regita_kelas = "SI-1A"
lulus = True

# Menampilkan output
print("Nama: ", regita_nama)
print("Umur: ", regita_umur, "tahun")
print("Tinggi Badan: ", regita_tinggi, "cm")
print("Program Studi: ", regita_program_studi)
print("Kelas: ", regita_kelas)
print("Jenis Kelamin: ", regita_jenis_kelamin)

# Menampilkan status kelulusan
if lulus:
    print("Status: Alumni")
else:
    print("Status: Mahasiswa aktif")