# Buat file dengan nama aritmatika_NIM.py
# Buatb program untuk operator artimatika dalam python
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input() 
#  Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_1015 = int(input("Masukkan angka pertama: "))
angka2_1015 = int(input("Masukkan angka kedua: "))

#Penjumlahan
hasil_1015 = angka1_1015 + angka2_1015
print("\nOperator Penjumlahan")
print("Hasil =", hasil_1015)

#Pengurangan
hasil_1015 = angka1_1015 - angka2_1015
print("\nOperator Pengurangan")
print("Hasil =", hasil_1015)

#Perkalian
hasil_1015 = angka1_1015 * angka2_1015
print("\nOperator Perkalian")
print("Hasil =", hasil_1015)

#Pembagian, Pembagian bulat, dan sisa bagi
if angka2_1015 != 0:
    hasil_1015 = angka1_1015 / angka2_1015
    print("\nOperator Pembagian")
    print("Hasil =", hasil_1015)

    hasil_1015 = angka1_1015 // angka2_1015
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_1015)

    hasil_1015 = angka1_1015 % angka2_1015
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_1015)

else:
    print("Angka kedua tidak boleh bernilai 0")

# Pangkat
hasil_1015 = angka1_1015 ** angka2_1015
print("\nOperator Pangkat")
print("Hasil =", hasil_1015)