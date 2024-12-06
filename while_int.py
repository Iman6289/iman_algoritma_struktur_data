a = int(input('masukan bilangan ganjil lebih dari 50: '))

while  a % 2 != 1 or a <= 50:
    a = int(input('salah,masukan lagi: '))

print('benar')