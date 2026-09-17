# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam python

angka1_1015 = int(input("Input Angka-1: "))
angka2_1015 = int(input("Input Angka-2: "))

print("\nNilai awal angka1 = ", angka1_1015)
print("Nilai angka2 = ", angka2_1015)

# assignment biasa
hasil_1015 = angka1_1015
print("Assignment Biasa (=)")
print("Hasil =", hasil_1015)

# assignment penambahan
hasil_1015 = angka1_1015 
hasil_1015 += angka2_1015
print("\nAssignment Penambahan (+=)")
print("Hasil =", hasil_1015)

#asignment pengurangan
hasil_1015 = angka1_1015
hasil_1015 -= angka2_1015
print("\nAssignment Pengurangan (-=)")
print("Hasil =", hasil_1015)

# assignment perkalian
hasil_1015 = angka1_1015
hasil_1015 *= angka2_1015
print("\nAssignment Perkalian (*=)")
print("Hasil =", hasil_1015)

# assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_1015 != 0:
    hasil_1015 = angka1_1015
    hasil_1015 /= angka2_1015
    print("\nAssignment Pembagian (/=)")
    print("Hasil =", hasil_1015)
    #Operator tambahan
    hasil_1015 = angka1_1015
    hasil_1015 //= angka2_1015
    print("\nAssignment Pembagian Bulat (//=)")
    print("Hasil =", hasil_1015)

    hasil_1015 = angka1_1015
    hasil_1015 %= angka2_1015
    print("\nAssignment Sisa Bagi (%=)")
    print("Hasil =", hasil_1015)

else:
    print("Pembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0")

# Operator tambahan: assigment pangkat
hasil_1015 = angka1_1015
hasil_1015 **= angka2_1015
print("\nAssignment Pangkat (**=)")
print("Hasil =", hasil_1015)
