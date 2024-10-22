# Memasukan variabel
jml_karyawan = int(input("Masukan jml_karyawan: "))
gaji_pokok = float(input("Masukan gaji_pokok: "))
pajak = float
tunjangan = float
jml_gaji = float

# Proses menghitung gaji
pajak = 0.1 * gaji_pokok
tunjangan = 0.2 * gaji_pokok
gaji_bersih = gaji_pokok + tunjangan + pajak
jml_gaji = gaji_bersih * jml_karyawan

# Menampilkan output
print("Detail tunjangan perorang: ", tunjangan)
print("Detail_pajak: ", pajak)
print("Detail_gaji ", jml_karyawan, "orang:", "Rp.", jml_gaji)
