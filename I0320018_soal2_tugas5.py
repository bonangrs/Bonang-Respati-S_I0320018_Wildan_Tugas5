nama = input('Masukkan nama: ')
nilai = int(input('Masukkan nilai: '))

if nilai > 100 or nilai < 0:
    print('Nilai tidak valid untuk dikonversi')
else:
    if nilai >= 85:
        grade = 'A'
    elif nilai >= 80:
        grade = 'A-'
    elif nilai >= 75:
        grade = 'B+'
    elif nilai >= 70:
        grade = 'B'
    elif nilai >= 65:
        grade = 'C+'
    elif nilai >= 60:
        grade = 'C'
    else:
        grade = 'E'

    print('Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah', grade)