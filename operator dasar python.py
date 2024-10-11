#Operator aritmatika
a, b = 10, 3

print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
print(a, '/', b, '=', a / b)
print(a, '%', b, '=', a % b)
print(a, '**', b, '=', a ** b)
print(a, '//', b, '=', a //b)
#Operator komparasi atau perbandingan
# buat variabel a dan b dengan teknik squence ordering
a, b = 5, 10

print(a, '>', b, '=', a > b)
print(a, '<', b, '=', a < b)
print(a, '==', b, '=', a == b)
print(a, '!=', b, '=', a != b)
print(a, '>=', b, '=', a >= b)
print(a, '<=', b, '=', a <= b)
#Operator penugasan
# penugasan pertama
a = 10
print('a = 10 -> ', a)

a += 5
print('a += 5 -> ', a)

a -= 3
print('a -= 3 -> ', a)

a *= 6
print('a *= 6 -> ', a)

a /= 8
print('a /= 8 -> ', a)

# karena a jadi float, kita ubah lagi menjadi integer
a = int(a)

a %= 9
print('a %= 9 -> ', a)

a //= 6
print('a //= 6 -> ', a)

a **= 1
print('a **= 1 -> ', a)


a &= 2
print('a &= 2 -> ', a)

a |= 3
print('a |= 3 -> ', a)

a ^= 4
print('a ^= 4 -> ', a)

a >>= 4
print('a >>= 4 -> ', a)

a <<= 2
print('a <<= 4 -> ', a)
#Operator logika
print(True and True)
print(1 + 2 == 3 and True)
print('----')
print(False or 1 > 5)
print(False or 5 > 2)
print('----')
print(not(1 > 5))
print(not(1 < 5))
#Operator keanggotaan
perusahaan = 'Microsoft'
list_pulau = ['Jawa', 'Sumatra', 'Sulawesi']

# ini adalah dictionary, insyaallah akan kita pelajari
# di pertemuan-pertemuan yang akan datang
mahasiswa = {
  'nama': 'Lendis Fabri',
  'asal': 'Lamongan'
}

print(
  "Apakah 'c' ada di variabel perusahaan?",
  'c' in perusahaan
)
print(
  "Apakah 'z' tidak ada di variabel perusahaan?",
  'c' not in perusahaan
)
print(
  "Apakah 'Madura' ada di variabel list_pulau?",
  'Madura' in perusahaan
)
print(
  "Apakah 'Madura' tidak ada di variabel list_pulau?",
  'Madura' not in perusahaan
)
print(
  "Apakah atribut 'nama' ada di variabel mahasiswa?",
  'nama' in mahasiswa
)
#Operator identitas
a = 5
b = 5
list_a = [1, 2, 3]
list_b = [1, 2, 3]
nama_a = 'budi'
nama_b = 'budi'

# output True
print('a is b:', a is b)
# output False
print('a is not b:', a is not b)

# output False
print('list_a is list_b:', list_a is list_b)
# output True
print('list_a == list_b:', list_a == list_b)

# output True
print('nama_a is nama_b:', nama_a is nama_b)
# output False
print('nama_a is not nama_b:', nama_a is not nama_b)