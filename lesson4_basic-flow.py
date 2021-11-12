jumlah = 1
pertanyaan = f'ibu : beli susu {jumlah} botol'
print(pertanyaan)

jawaban = 'ok'
print(f'anak : {jawaban}')
print(f'\n-> anak pergi ke toko')

susu = 'ada'
telur = 'ada'
uang = 50000
hargasusu = 30000
keranjang = []

print('ibu : beli susu kalau ada dan uangnya cukup')
if susu == 'ada' and uang > hargasusu:
    print(f'\nsusu {susu} harganya {hargasusu}, uang {uang} cukup')
    jumlah = 1
    keranjang.append({'item':'susu', 'jumlah': jumlah})

    print('\nibu : beli telur 6 kalau ada')
    if telur == 'ada':
        jumlah = 6
        print(f'anak : telur {telur} beli {jumlah}')
        keranjang.append({'item': 'telur', 'jumlah': jumlah})
    else:
        print(f'anak : telur {telur} tidak beli telur')
else:
    print('tidak ada susu, -> tidak jadi beli')

print(f'\nbarang yang dibeli {keranjang}')

# dasdasdas
