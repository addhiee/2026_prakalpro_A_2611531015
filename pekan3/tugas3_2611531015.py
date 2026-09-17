# 1. INPUT DATA PELANGGAN DAN TRANSAKSI

print("=== SISTEM TRANSAKSI TOKO ===")
nama_1015 = input("Masukkan Nama Pelanggan : ")
status_1015 = input("Masukkan Status Pelanggan (member/nonmember) : ").strip().lower()
total_belanja_1015 = float(input("Masukkan Total Belanja : "))
jumlah_barang_1015 = int(input("Masukkan Jumlah Barang : "))
kode_promo_1015 = input("Masukkan Kode Promo : ").strip().upper()

# Daftar promo resmi
daftar_promo_1015 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# 2. OPERATOR KEANGGOTAAN (MEMBERSHIP)

# Memeriksa keberadaan kode promo dalam daftar promo
promo_tersedia_1015 = kode_promo_1015 in daftar_promo_1015
promo_tidak_tersedia_1015 = kode_promo_1015 not in daftar_promo_1015

# 3. OPERATOR PERBANDINGAN & LOGIKA

# Operator Perbandingan
min_belanja_1015 = total_belanja_1015 >= 200000
min_barang_1015 = jumlah_barang_1015 >= 3
is_member_1015 = status_1015 == "member"

# Operator Logika (and, or, not)
dapat_diskon_1015 = is_member_1015 and min_belanja_1015
dapat_promo_1015 = promo_tersedia_1015 or (min_barang_1015 and not (status_1015 == "nonmember"))

# 4. OPERATOR ARITMATIKA & PENUGASAN (AUGMENTED ASSIGNMENT)

# Menghitung besarnya diskon (10% jika dapat diskon)
diskon_1015 = total_belanja_1015 * 0.10 if dapat_diskon_1015 else 0.0

# Perhitungan Total Pembayaran
total_pembayaran_1015 = total_belanja_1015
total_pembayaran_1015 -= diskon_1015  

# Perhitungan Rata-rata Harga Barang
rata_harga_1015 = total_belanja_1015 / jumlah_barang_1015

# Sisa pembagian (Operator Aritmatika %)
sisa_barang_1015 = jumlah_barang_1015 % 3

# 5. OPERATOR IDENTITAS (IDENTITY)

objek_a_1015 = "member"
objek_b_1015 = input_status_temp = "mem" + "ber"


is_sama_nilai_1015 = (objek_a_1015 == objek_b_1015)
is_sama_identitas_1015 = (objek_a_1015 is objek_b_1015)
is_beda_identitas_1015 = (objek_a_1015 is not status_1015)

# 6. OPERATOR BITWISE

BIT_MEMBER_1015 = 0b0001
BIT_BELANJA_1015 = 0b0010
BIT_BARANG_1015 = 0b0100
BIT_PROMO_1015 = 0b1000

# Penggabungan kondisi menggunakan Bitwise OR (|)
kode_status_1015 = 0b0000
if is_member_1015:
    kode_status_1015 |= BIT_MEMBER_1015
if min_belanja_1015:
    kode_status_1015 |= BIT_BELANJA_1015
if min_barang_1015:
    kode_status_1015 |= BIT_BARANG_1015
if promo_tersedia_1015:
    kode_status_1015 |= BIT_PROMO_1015

# Pemeriksaan kondisi menggunakan Bitwise AND (&)
cek_member_1015 = kode_status_1015 & BIT_MEMBER_1015
cek_promo_1015 = kode_status_1015 & BIT_PROMO_1015

# Perbandingan status menggunakan Bitwise XOR (^)
kode_referensi_1015 = 0b1011  
beda_status_1015 = kode_status_1015 ^ kode_referensi_1015

# Bitwise geser kiri (<<)
shift_status_1015 = kode_status_1015 << 1

# 7. MENAMPILKAN OUTPUT SESUAI FORMAT KETENTUAN 
print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan        : {nama_1015}")
print(f"Status Pelanggan      : {status_1015}")
print(f"Total Belanja         : Rp{int(total_belanja_1015)}")
print(f"Jumlah Barang         : {jumlah_barang_1015}")
print(f"Kode Promo            : {kode_promo_1015}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000   : {min_belanja_1015}")
print(f"Jumlah Barang >= 3    : {min_barang_1015}")
print(f"Status Member         : {is_member_1015}")
print(f"Kode Promo Tersedia   : {promo_tersedia_1015}")
print(f"Mendapatkan Diskon    : {dapat_diskon_1015}")
print(f"Mendapatkan Promo     : {dapat_promo_1015}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                : Rp{int(diskon_1015)}")
print(f"Total Pembayaran      : Rp{int(total_pembayaran_1015)}")
print(f"Rata-rata Harga Barang: Rp{rata_harga_1015:.2f}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses        : {bin(kode_status_1015)[2:].zfill(4)}")
print(f"Member Access         : {bool(cek_member_1015)}")
print(f"Promo Access          : {bool(cek_promo_1015)}")
print(f"Free Shipping Access  : {kode_promo_1015 == 'GRATISONGKIR'}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print(f"Kode Biner    : {bin(kode_status_1015)[2:].zfill(4)}")
print(f"Kode Desimal  : {kode_status_1015}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{bin(kode_status_1015)[2:].zfill(4)} & 0001")
print(f"Hasil Biner   : {bin(cek_member_1015)[2:].zfill(4)}")
print(f"Hasil Desimal : {cek_member_1015}")

print("\nCek Promo")
print(f"{bin(kode_status_1015)[2:].zfill(4)} & 1000")
print(f"Hasil Biner   : {bin(cek_promo_1015)[2:].zfill(4)}")
print(f"Hasil Desimal : {cek_promo_1015}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {bin(kode_status_1015)[2:].zfill(4)}")
print(f"Kode Referensi : {bin(kode_referensi_1015)[2:].zfill(4)}")
print(f"{bin(kode_status_1015)[2:].zfill(4)} ^ {bin(kode_referensi_1015)[2:].zfill(4)}")
print(f"Hasil Biner   : {bin(beda_status_1015)[2:].zfill(4)}")
print(f"Hasil Desimal : {beda_status_1015}")

print("\n=== Shift ===")
print(f"{bin(kode_status_1015)[2:].zfill(4)} << 1")
print(f"Hasil Biner   : {bin(shift_status_1015)[2:].zfill(5)}")
print(f"Hasil Desimal : {shift_status_1015}")

print("\n=== SELESAI ===")