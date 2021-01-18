
class Ogrenci():
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinif):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinif = ogrenciSinif


class Soru():
    def __init__(self, dogru_sayisi, yanlis_sayisi, net_sayisi, puan):
        self.dogru_sayisi = dogru_sayisi
        self.yanlis_sayisi = yanlis_sayisi
        self.net_sayisi = net_sayisi
        self.puan = puan


    def netSayisi(self, dogru_sayisi, yanlis_sayisi):
        self.net_sayisi = dogru_sayisi - float(yanlis_sayisi * 0.25)
        return self.net_sayisi

    def hesapla(self, net_sayisi):
        self.puan = net_sayisi * 2
        return self.puan


ogrenci = Ogrenci('Emre', 'Özbey', '3')

sonuc= Soru(0, 0, 0, 0 )

dogru_sayisi = int(input("Lütfen doğru sayısını giriniz: "))
yanlis_sayisi = int(input("Lütfen yanlış sayısını giriniz: "))

sonuc.netSayisi(dogru_sayisi, yanlis_sayisi)


print("""
        Ad         : {}
        Soyad      : {}
        Sınıfı     : {}
        Sınav Puanı: {}
        """.format(ogrenci.ogrenciAdi, ogrenci.ogrenciSoyadi, ogrenci.ogrenciSinif, sonuc.hesapla(sonuc.net_sayisi)))