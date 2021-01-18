__author__ = 'Emre'


def bolunen_sayı(min_sayi, max_sayi, bolunecek_sayi):

    liste1= list()

    for i in range(min_sayi, max_sayi):
        if(i % bolunecek_sayi == 0):
            liste1.append(i)



    return liste1

print('belirtilen aralıktaki istenen sayıya bölünebilen değerler:', bolunen_sayı(5,10,2) )
