# rumus: sisi * sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# rumus: sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

# contoh peengguna   
sisi = 5
print("luas persegi:", luas_persegi(sisi))
print("volume kubus:", volume_persegi(sisi))