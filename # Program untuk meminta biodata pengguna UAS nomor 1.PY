def main():
    print("=== Program Informasi Pengguna ===\n")

    # Meminta input dari pengguna
    nama = input("Masukkan nama Anda: Iman")
    usia = input("Masukkan usia Anda: 18 tahun")
    alamat = input("Masukkan alamat Anda: Desa penyak")
    hobi = input("Masukkan hobi Anda: Beramain game")

    # Menampilkan informasi dalam format yang rapi
    print("\n=== Informasi Anda ===")
    print(f"Nama   : {nama} Iman")
    print(f"Usia   : {usia} 18 tahun")
    print(f"Alamat : {alamat} Desa penyak")
    print(f"Hobi   : {hobi} Bermain game")

if __name__ == "__main__":
    main()