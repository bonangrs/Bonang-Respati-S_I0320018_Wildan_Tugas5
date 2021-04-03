nama = input('Masukkan nama Anda: ')
gender = input('Masukkan jenis kelamin Anda (P/L): ')
if gender.upper() == 'P':
    print('Selamat datang, Nyonya', nama + '!')
elif gender.upper() == 'L':
    print('Selamat datang, Tuan', nama + '!')
else:
    pass