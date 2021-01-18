__author__ = 'Emre'

def sayi_okunusu(index1, index2):
    birler = ['','bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz' ]
    onlar = ['', 'On', 'Yirmi', 'Otuz', 'Kırk', 'Elli', 'Altmış', 'Yetmiş', 'Seksen', 'Doksan']

    print(onlar[index2] + ' ' + birler[index1])

def sayi_atama(atanan_sayi):

    if(atanan_sayi <= 99 and atanan_sayi >= 10):
        sayi = atanan_sayi
        birinci = sayi % 10
        ikinci = sayi // 10
    else:
         print('Lütfen 2 basamaklı bir sayı giriniz!!!')
    sayi_okunusu(birinci, ikinci)

sayi_atama(50)