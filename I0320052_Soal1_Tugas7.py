# buat 1 program menggunakan fungsi string
# minimal 3 jenis fungsi string

print('Soal 1\n')
print('Masukkan string')
string = str(input('==> '))
print('\n')
print('1. Metode Capitalize ()')
print('2. Metode Center ()')
print('3. Metode Count ()')
print('4. Metode Endswith ()')
print('5. Metode Find ()')
print('6. Metode Index ()')
print('7. Metode Replace ()')
print('8. Metode Upper () dan Lower ()\n')
pil = int(input('Pilih perlakuan untuk string : '))
print('\n')

if pil == 1:
    kapital = string.capitalize()
    print('=> ', kapital)
elif pil == 2:
    tengah = string.center(50, '=')
    print(tengah)
elif pil == 3:
    count1 = str(input('Masukkan karakter yang ingin dihitung : '))
    a = string.count(count1)
    print('\nJumlah karakter "', count1, '" : ', a)
elif pil == 4:
    cek = str(input('Masukkan sebuah kata untuk pengecekan : '))
    print('\nApakah string diakhiri oleh kata "', cek, '" : ', string.endswith(cek))
elif pil == 5:
    find1 = str(input('Input karakter yang ingin ditemukan : '))
    if string.find(find1) != -1:
        print('\nKarakter ', find1, ' pertama ada di indeks : ', string.find(find1))
    else:
        print('\nKarakter ', find1, ' pertama ada di indeks : ', string.find(find1))
        print('Note : -1 berarti karakter tidak ditemukan di string')
elif pil == 6:
    print('Akan error apabila indeks tidak ditemukan.')
    indeks = str(input('\nInput karakter yang ingin di indeks : '))
    if string.index(indeks):
        print('Karekter', indeks, 'berada di indeks : ', string.index(indeks))
elif pil == 7:
    print('String anda : %s\n' % string)
    lama = str(input('Masukkan kata yang ingin diganti : '))
    baru = str(input('Masukkan kata yang baru : '))
    print('\nReplace "', lama, '"', 'menjadi', '"', baru, '"', ', hasil =  ', string.replace(lama, baru))
else:
    print('Upper string = ', string.upper())
    print('Lower string = ', string.lower())
input()
