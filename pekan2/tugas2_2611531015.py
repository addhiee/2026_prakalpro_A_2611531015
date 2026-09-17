print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_1015 = input("Masukkan Nama Mahasiswa : ")
kelamin_1015 = input("Masukkan Jenis Kelamin (L/P): ")
umur_1015 = int(input("Masukkan Umur : "))
skor_1015 = float(input("Masukkan Skor Tes Awal : "))

alamat_1015 = """
Lubuk Gading VI,
Kecamatan Koto Tangah,
Kota Padang,
Sumatera Barat,
Indonesia
"""
from typing import Final
kkm_1015: Final = 75.0
token_1015 = 100+3j
lulus_1015 = skor_1015 > kkm_1015

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_1015," | ",type(nama_1015))
print("Jenis Kelamin : ",kelamin_1015," | ",type(kelamin_1015))
print("Alamat Domisili : ",alamat_1015," | ",type(alamat_1015))
print("Umur : ",umur_1015," tahun | ",type(umur_1015))
print("Skor Tes Awal : ",skor_1015," | ",type(skor_1015))
print("ID Token Sinyal: ",token_1015," | ",type(token_1015))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ",kkm_1015," | ",type(kkm_1015))
print("Apakah Dinyatakan Lulus?: ",lulus_1015," | ",type(lulus_1015))