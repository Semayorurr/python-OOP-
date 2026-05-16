from abc import ABC,abstractmethod
class menu:
    def goster(self):
        print("1.Kitap Ekle")
        print("2.Kitap Sil")
        print("3.Kitap Güncelle")
        print("4.Kitapları listele")
        print("5.Dergi Ekle")
        print("6.Dergi Sil")
        print("7.Dergi Güncelle")
        print("8.Dergileri Listele")
        print("9.Çıkış")
class kaynak(ABC):
    @abstractmethod
    def __init__(self,baslik,kayitNo,sayfaSayisi,yayinTarihi,yayinEvi):
        self.baslik = baslik
        self.kayitNo = kayitNo
        self.sayfaSayisi = sayfaSayisi
        self.yayinTarihi = yayinTarihi
        self.yayinEvi = yayinEvi
class kitap(kaynak):
    def __init__(self,baslik,kayitNo,sayfaSayisi,yayinTarihi,yayinEvi,yazar,tür,baskiSayisi):
        super().__init__(baslik,kayitNo,sayfaSayisi,yayinTarihi,yayinEvi)
        self.yazar = yazar
        self.tür=tür
        self.baskiSayisi=baskiSayisi
class dergi(kaynak):
    def __init__(self,baslik,kayitNo,sayfaSayisi,yayinTarihi,yayinEvi,sayiNo,editör):
        super().__init__(baslik,kayitNo,sayfaSayisi,yayinTarihi,yayinEvi)
        self.sayiNo=sayiNo
        self.editör=editör
