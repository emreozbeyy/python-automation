__author__ = 'Emre'


class Insan():
    def __init__(self, ad="Emre", soyad="Özbey", yas=26, ulke="Türkiye", sehir="Sinop", yetenekler=[]):

        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = yetenekler


    def bilgileri_goster(self):
        print("""
        İSİM : {}
        SOYAD : {}
        YAŞ : {}
        ÜLKE : {}
        ŞEHİR : {}
        YETENEKLER : {}
        """.format(self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler))

    def yetenek_ekle(self, yeni_yetenek):
        self.yetenekler.append(yeni_yetenek)

kisi = Insan()
kisi.yetenek_ekle(["Python","Yüzmek","Araba sürmek","Fransızca"])

kisi.bilgileri_goster()


