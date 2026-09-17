# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()

print("===========================")
print("3. OPERATOR BITWISE")
print("===========================")

angka1_1015 = int(input("Masukkan angka bitwise-1: "))
angka2_1015 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_1015, "| biner =", bin(angka1_1015))
print("angka2 =", angka2_1015, "| biner =", bin(angka2_1015))

# Bitwise AND
hasil_1015 = angka1_1015 & angka2_1015
print("\nOperator Bitwise AND (&)")
print(angka1_1015, "&", angka2_1015, "=", hasil_1015)
print("Biner hasil=", bin(hasil_1015))
print("Biner hasil (8 bit) =", format(hasil_1015, '08b'))

# Bitwise OR
hasil_1015 = angka1_1015 | angka2_1015
print("\nOperator Bitwise OR (|)")
print(angka1_1015, "|", angka2_1015, "=", hasil_1015)
print("Biner hasil=", bin(hasil_1015))
print("Biner hasil (8 bit) =", format(hasil_1015, '08b'))

# Bitwise XOR
hasil_1015 = angka1_1015 ^ angka2_1015
print("\nOperator Bitwise XOR (^)")
print(angka1_1015, "^", angka2_1015, "=", hasil_1015)
print("Biner hasil=", bin(hasil_1015))
print("Biner hasil (8 bit) =", format(hasil_1015, '08b'))

# Bitwise NOT
hasil_1015 = ~angka1_1015
print("\nOperator Bitwise NOT (~)")
print("~", angka1_1015, "=", hasil_1015)
print("Biner hasil=", bin(hasil_1015))
print("Biner hasil (8 bit) =", format(hasil_1015, '08b'))

# Bitwise geser kiri
jumlah_geser_1015 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_1015 = angka1_1015 << jumlah_geser_1015
print("\nOperator Bitwise Geser Kiri (<<)")
print(angka1_1015, "<<", jumlah_geser_1015, "=", hasil_1015)
print("Biner hasil=", bin(hasil_1015))
print("Biner hasil (8 bit) =", format(hasil_1015, '08b'))

# Bitwise geser kanan
hasil_1015 = angka1_1015 >> jumlah_geser_1015
print("\nOperator Bitwise Geser Kanan (>>)")
print(angka1_1015, ">>", jumlah_geser_1015, "=", hasil_1015)
print("Biner hasil=", bin(hasil_1015))
print("Biner hasil (8 bit) =", format(hasil_1015, '08b'))