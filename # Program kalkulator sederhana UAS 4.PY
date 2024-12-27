# Program kalkulator sederhana

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Pembagi tidak boleh 0."

def kalkulator():
    print("=== Kalkulator Sederhana ===")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    
    # Input pilihan operasi
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    # Meminta input angka
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print(f"{angka1} + {angka2} = {tambah(angka1, angka2)}")
    elif pilihan == '2':
        print(f"{angka1} - {angka2} = {kurang(angka1, angka2)}")
    elif pilihan == '3':
        print(f"{angka1} * {angka2} = {kali(angka1, angka2)}")
    elif pilihan == '4':
        print(f"{angka1} / {angka2} = {bagi(angka1, angka2)}")
    else:
        print("Pilihan tidak valid!")

# Memanggil fungsi kalkulator
if __name__ == "__main__":
    kalkulator()
