# membuat variabel global
nama = "Belajar code"
versi = "1.0.0"

def help():
    # ini variabel lokal 
    nama = "programku"
    versi = "1.0.1"
    # mengakses variabel lokal
    print ("Nama: %s" % nama)
    print("Versi: %s" % versi)

# mengakses variabel lokal
print("Nama: %s" % nama)
print("Versi: %s" % versi) 

# memanggil fungsi help
help()