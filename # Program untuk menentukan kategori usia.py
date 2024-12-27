# Program untuk menentukan kategori usia

def kategori_usia(usia):
    if usia < 13:
        return "Anak-anak"
    elif 13 <= usia <= 17:
        return "Remaja"
    elif 18 <= usia <= 64:
        return "Dewasa"
    else:
        return "Lansia"

def main():
    # Meminta input usia dari pengguna
    usia = int(input("Masukkan usia Anda: 18 tahun "))

    # Menentukan kategori usia dan menampilkan hasil
    kategori = kategori_usia(usia)
    print(f"Kategori usia Anda: {kategori}")

# Memanggil fungsi utama
if __name__ == "__main__":
    main()
