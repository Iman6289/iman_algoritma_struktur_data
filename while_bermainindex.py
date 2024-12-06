listkota = ['jakarta','surabaya','bekasi','solo','joqyakarta''semarang','makasar']

kotayangDicari = input('masukan nama kota yang anda cari: ')

i = 0
while i < len(listkota):
    if listkota[i].lower() == kotayangDicari.lower():
        print('berhasil di temukan', i)
        break
    
    print('bukan', listkota[i])
    i += 1

else:
     print('maaf,kota yang anda cari tidak ditemukan')