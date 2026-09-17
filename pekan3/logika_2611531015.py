# buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()
# Program   operator logika dalam python

# Memasukkan Nilai boolean
# input tidak peka terhadap huruf besar dan kecil
a1_1015 = ("input nilai boolean-1 (True/False): "). strip().lower() == "true"
a2_1015 = ("input nilai boolean-2 (True/False): "). strip().lower() == "true"

print ("\nA1= ", a1_1015)
print ("A2= ", a2_1015)

# konjungsi: bernilai true jika keduanya true
hasil_1015 = a1_1015 and a2_1015
print("\nOperator Konjungsi (AND)")
print("A1 and A2 =", hasil_1015)

# Disjungsi: bernilai true jika salah satu true
hasil_1015 = a1_1015 or a2_1015
print("\nOperator Disjungsi (OR)")
print("A1 or A2 =", hasil_1015)

# Negasi A1: membalik nilai A1
hasil_1015 = not a1_1015
print("\nOperator Negasi (NOT)")
print("not A1 =", hasil_1015)

# Negasi A2: membalik nilai A2
hasil_1015 = not a2_1015
print("not A2 =", hasil_1015)

# XOR: bernilai True jika kedua nilai berbeda
hasil_1015 = a1_1015 != a2_1015
print("\nDijungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_1015)