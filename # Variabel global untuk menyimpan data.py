#variabel global untuk menyimpan buku

buku = []


#fungsi untuk menampilkan semua data
def show_data():
    if len (buku) <= 0:
        print("belum ada data")
          
    else:
        for indeks in range(len(buku)):
            print(f"[{indeks}] {buku[indeks]}")
            
#fungsi menambahkan data
def insert_data():
    buku_baru = input("judul buku: ")
    buku.append(buku_baru)
    print("data berhasil di tambahkan")
#fungsi edit data
def edit_data():
    show_data()
    indeks = int(input("masukan id buku: "))
    if indeks > len(buku):
        print("ID SALAH")
    else:
        judul_baru = input("judul baru : ")
        buku[indeks] = judul_baru
        
#fungsi edit data
def delete_data():
    show_data()
    indeks = int(input("masukan id buku: "))
    if indeks > len(buku):
        print("ID SALAH")
    else:
        buku.remove(buku[indeks])
        
#fungsi show menu
def show_menu():
    print("\n")
    print("------ MENU -----")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    
    menu = input("PILIH MENU> ")
    print("\n")
    
    if int(menu) == 1:
        show_data()  
    elif int(menu) == 2:
        insert_data()
    elif int(menu) == 3:
        edit_data()
    elif int(menu) == 4:
        delete_data()
    elif int(menu) == 5:
        exit()
    else:
        print("salah pilih!")
        
if __name__ == "__main__":
    while True:
        show_menu()
        