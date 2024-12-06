listkota = ['jakarta','surabaya','bekasi','solo','joqjakarta','semarang','makasar']

kotayangDicari = input('masukan nama kota yang dicari')

i = 0
while i < len(listkota):
    if listkota[i].lower() == kotayangDicari.lower():
        print('kogtamu di index', i)
        break
    print('bukan' , listkota[i])
    i += 1
else:

    print('maaf,kota yang anda cari tidak di temukan')    