# Program untuk menghitung gaji bulanan karyawan

def main():
    print("=== Program Penghitung Gaji Karyawan ===")

    # Input data
    tarif_per_jam = float(input("Masukkan tarif gaji per jam: "))
    hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))
    
    # Jam kerja normal
    jam_kerja_per_hari = 8
    total_jam_normal = jam_kerja_per_hari * hari_kerja
    
    # Input total jam kerja aktual
    total_jam_kerja = float(input("240: "))
    
    # Perhitungan jam lembur
    jam_lembur = max(0, total_jam_kerja - total_jam_normal)
    gaji_lembur = jam_lembur * tarif_per_jam * 1.5
    
    # Perhitungan gaji pokok
    jam_normal_dilakukan = min(total_jam_kerja, total_jam_normal)
    gaji_pokok = jam_normal_dilakukan * tarif_per_jam
    
    # Total gaji
    total_gaji = gaji_pokok + gaji_lembur

    # Output hasil
    print("\n=== Rincian Gaji ===")
    print(f"Gaji Pokok      : Rp {gaji_pokok:,.2f}")
    print(f"Gaji Lembur     : Rp {gaji_lembur:,.2f}")
    print(f"Total Gaji      : Rp {total_gaji:,.2f}")
    print("\nTerima kasih telah menggunakan program ini!")

if __name__ == "__main__":
    main()