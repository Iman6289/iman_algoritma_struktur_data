def cetak_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    """
    Fungsi untuk menghitung dan mencetak gaji berdasarkan jam kerja normal dan lembur.
    
    Parameters:
    tarif_per_jam (float): Tarif gaji per jam.
    jam_kerja_per_hari (float): Jam kerja per hari.
    hari_kerja (int): Jumlah hari kerja dalam sebulan.
    """
    print("=== Perhitungan Gaji ===")
    
    # Hitung total jam kerja normal
    total_jam_normal = jam_kerja_per_hari * hari_kerja
    
    # Input total jam kerja aktual
    total_jam_kerja = float(input("Masukkan total jam kerja aktual dalam sebulan: "))
    
    # Hitung jam lembur
    jam_lembur = max(0, total_jam_kerja - total_jam_normal)
    gaji_lembur = jam_lembur * tarif_per_jam * 1.5
    
    # Hitung gaji pokok
    jam_normal_dilakukan = min(total_jam_kerja, total_jam_normal)
    gaji_pokok = jam_normal_dilakukan * tarif_per_jam
    
    # Hitung total gaji
    total_gaji = gaji_pokok + gaji_lembur

    # Output hasil
    print(f"\nGaji Pokok      : Rp {gaji_pokok:,.2f}")
    print(f"Gaji Lembur     : Rp {gaji_lembur:,.2f}")
    print(f"Total Gaji      : Rp {total_gaji:,.2f}")
    print("\nTerima kasih!")

# Contoh penggunaan fungsi
if _name_ == "_main_":
    tarif_per_jam = float(input("Masukkan tarif gaji per jam: "))
    jam_kerja_per_hari = float(input("Masukkan jam kerja per hari: "))
    hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))
    cetak_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja)