# buat 1 program menggunakan fungsi numerik
# minimal 3 jenis fungsi numerik
import math
print('Soal 2\n')
print('Masukkan bilangan anda.')
numerik = input('==> ')
numerik1 = float(numerik)
print('\n')
print('1. Metode Abs ()')
print('2. Metode Ceil ()')
print('3. Metode Fabs ()')
print('4. Metode Floor ()')
print('5. Metode Min () dan Max ()')
print('6. Metode Sqrt ()')
print('7. Metode Choice ()\n')
pil = int(input('Pilih perlakuan untuk bilangan anda : '))
print('\n')

if pil == 1:
    numerik0 = int(numerik)
    print('Fungsi ini akan mengembalikan bilangan anda menjadi nilai mutlaknya\n')
    print('Bilangan anda : ', numerik)
    print('|', numerik, '| :', abs(numerik0))
elif pil == 2:
    print('Fungsi ini akan melakukan pembulatan keatas\n')
    print('Bilangan anda : ', numerik1)
    print('Hasil pembulatan : ', math.ceil(numerik1))
elif pil == 3:
    print('Fungsi ini akan mengembalikan nilai absolut\n')
    print('Bilangan anda : ', numerik)
    print('Hasil : ', math.fabs(numerik1))
elif pil == 4:
    print('Fungsi ini akan melakukan pembulatan kebawah\n')
    print('Bilangan anda : ', numerik)
    print('Hasil pembulatan : ', math.floor(numerik1))
elif pil == 5:
    print('Fungsi untuk mencari milai minimum maupun maksimum\n')
    a = float(numerik)
    b = float(input('Masukkan bilangan tambahan : '))
    c = float(input('Masukkan bilangan tambahan : '))
    print('Data bilangan anda : ', a, ',', b, ', dan', c)
    choice = str(input('\nmin/max : '))
    if choice == 'min':
        print('Nilai minimun dari data anda : ', min(a, b, c))
    else:
        print('Nilai maksimum dari data anda : ', max(a, b, c))
elif pil == 6:
    print('Fungsi ini digunakan untuk menghitung nilai akar kuadrat\n')
    print('Bilangan anda : ', numerik1)
    print('Nilai sqrt bilangan anda : ', math.sqrt(numerik1))
else:
    print('Fungsi ini akan mengambil secara acak nilai bilangan anda')
    import random
    a = numerik1
    b = float(input('Masukkan bilangan selanjutnya : '))
    c = float(input('Masukkan bilangan selanjutnya : '))
    d = float(input('Masukkan bilangan selanjutnya : '))
    data = [a, b, c, d]
    print('Data anda : ', data)
    print('Pengambilan acak ke-1 : ', random.choice(data))
    print('Pengambilan acak ke-2 : ', random.choice(data))
    print('Pengambilan acak ke-3 : ', random.choice(data))
    print('Pengambilan acak ke-4 : ', random.choice(data))
input()
