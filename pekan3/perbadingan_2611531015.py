# Buat file dengan nama perbadingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam python

angka1_1015 = int(input("Masukkan angka pertama: "))
angka2_1015 = int(input("Masukkan angka kedua: "))

# Lebih besar dari
hasil_1015 = angka1_1015 > angka2_1015
print("\nOperator Lebih Besar Dari")
print("angka1 > angka2 =", hasil_1015)

# Lebih kecil dari
hasil_1015 = angka1_1015 < angka2_1015
print("\nOperator Lebih Kecil Dari")
print("angka1 < angka2 =", hasil_1015)

# Lebih besar dari atau sama dengan
hasil_1015 = angka1_1015 >= angka2_1015
print("\nOperator Lebih Besar Dari atau Sama Dengan")
print("angka1 >= angka2 =", hasil_1015)

# Lebih kecil dari atau sama dengan
hasil_1015 = angka1_1015 <= angka2_1015
print("\nOperator Lebih Kecil Dari atau Sama Dengan")
print("angka1 <= angka2 =", hasil_1015)

# Sama dengan
hasil_1015 = angka1_1015 == angka2_1015
print("\nOperator Sama Dengan")
print("angka1 == angka2 =", hasil_1015)

# Tidak sama dengan
hasil_1015 = angka1_1015 != angka2_1015
print("\nOperator Tidak Sama Dengan")
print("angka1 != angka2 =", hasil_1015)

# Tambahan: Perbadingan berantai dalam python
hasil_1015 = 0 < angka1_1015 < 100
print("\nOperator Perbandingan Berantai")
print("0 < angka1 < 100 =", hasil_1015)

hasil_1015 = 0 < angka2_1015 < 100
print("0 < angka2 < 100 =", hasil_1015)