__author__ = 'Emre'
print('Lütfen birinci vize notunuzu giriniz(0-100): ')
vize1 = int(input())
print('Lütfen ikinci vize notunuzu giriniz(0-100): ')
vize2 = int(input())
print('Lütfen final notunuzu giriniz(0-100): ')
final = int(input())

not_ort = vize1 * 0.3 + vize2 * 0.3 + final * 0.4
print('Not Ortalamanız: ', not_ort)
print('Harf Notunuz: ')

if not_ort >= 90:
    print('AA')
elif not_ort >= 85:
    print('BA')
elif not_ort >= 80:
    print('BB')
elif not_ort >= 75:
    print('CB')
elif not_ort >= 70:
    print('CC')
elif not_ort >= 65:
    print('DC')
elif not_ort >= 60:
    print('DD')
elif not_ort >= 55:
    print('FD')
else:
    print('FF')
