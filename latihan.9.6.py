# Nilai diinput user
alas = float(input("Masukkan panjang alas jajaran genjang: "))
tinggi = float(input("Masukkan tinggi jajaran genjang: "))
sisi_a = float(input("Masukkan panjang sisi a: "))
sisi_b = float(input("Masukkan panjang sisi b: "))

# Menghitung luas dan keliling
luas = (alas * tinggi)
keliling = 2 * (sisi_a + sisi_b)

# Menampilkan hasil
print("Luas jajaran genjang adalah: ", luas, "cm")
print("Keliling jajaran genjang adalah: ", keliling, "cm")
