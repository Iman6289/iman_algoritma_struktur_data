listkora = ['jakarta','surabaya','depok','bekasi','solo','joqjakarta','semarang','makasar']

kotaYangDicari = input('ketik nama kota yang kamu cari')

for i, kota in enumerate(listkota):
    # kita ubah katanya ke lowercase agar 
    # menjadi case insensitive
    if kota.lower() == kotaYangDicari.lower():
        print('kota yang anda cari berada pda indeks', i)
        break
    else:
        prin('maaf,kota yang anda cari tidak ada')