# user menginput
jarak = float(input("Masukan jarak: "))

# Deklarasi 
harga_1_km = 4500
harga_selanjutanya = 2000

#Proses 
if jarak <= 1:
   harga_sewa = harga_1_km 
else:
    harga_sewa = harga_1_km + (jarak - 1) + harga_selanjutanya

    # Menampilkan output
    print("Total harga sewa", "Rp.", harga_sewa)



    
