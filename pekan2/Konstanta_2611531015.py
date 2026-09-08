# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# Nama variabel ditambah 4 digit nim terakhir contoh jari_1234

from typing import Final
PI: Final = 3.14
print("pi: %f" %(PI))
jari_1015 = float(input('Masukkan nilai jari-jari: '))
luas_1015 = PI * jari_1015 * jari_1015
print("luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1015, luas_1015))