# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("===========================")
print("1. OPERATOR KEANGGOTAAN")
print("===========================")

# Input beberapa data yang dipisahkan dengan koma
input_data_1015 = input("Masukkan beberapa data (pisahkan dengan koma): ")

# Mengubah input menjadi list integer
data_1015 = [int(angka.strip()) for angka in input_data_1015.split(',')]

nilai_dicari_1015 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_1015 = nilai_dicari_1015 in data_1015
print("\nOperator keanggotaan IN")
print(nilai_dicari_1015, "in", data_1015, "=", hasil_1015)

# Operator not in  
hasil_1015 = nilai_dicari_1015 not in data_1015
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_1015, "not in", data_1015, "=", hasil_1015)

print("\n===========================")
print("2. OPERATOR IDENTITAS")
print("===========================")

# objek1 menggunakan list dari input pengguna
objek1_1015 = data_1015

# objek2 merujuk pada objek yang sama dengan objek1
objek2_1015 = objek1_1015

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_1015 = data_1015.copy()

print("objek1 =", objek1_1015)
print("objek2 =", objek2_1015)
print("objek3 =", objek3_1015)

# Operator is
hasil_1015 = objek1_1015 is objek2_1015
print("\nOperator Identitas IS")
print("objek1 is objek2 =", hasil_1015)

# Operator is not
hasil_1015 = objek1_1015 is not objek3_1015
print("\nOperator Identitas IS NOT")
print("objek1 is not objek3 =", hasil_1015)

# Membandingkan identitas dan nilai
print("\nMembandingkan identitas dan nilai:")
print("objek1 is objek3 =", objek1_1015 is objek3_1015)
print("objek1 == objek3 =", objek1_1015 == objek3_1015)