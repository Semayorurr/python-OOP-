from abc import ABC,abstractmethod
class menu:
    @staticmethod
    def goster(self):
        print("|-------Hoşgeldiniz-------|")
        print("|------1.Kitap Ekle-------|")
        print("|------2.Kitap Sil--------|")
        print("|------3.Kitap Güncelle---|")
        print("|------4.Kitapları listele|")
        print("|------5.Dergi Ekle-------|")
        print("|------6.Dergi Sil--------|")
        print("|------7.Dergi Güncelle---|")
        print("|------8.Dergileri Listele|")
        print("|------9.Çıkış------------|")
class kaynak(ABC):
    @abstractmethod
    def __init__(self,baslik,kayitNo,sayfaSayisi,yayinTarihi,yayinEvi):
        self.baslik = baslik
        self.kayitNo = kayitNo
        self.sayfaSayisi = sayfaSayisi
        self.yayinTarihi = yayinTarihi
        self.yayinEvi = yayinEvi
    @property
    def baslik(self):
        return self._baslik
    @baslik.setter
    def baslik(self,value):
        self._baslik = value
    @property
    def kayitNo(self):
        return self._kayitNo
    @kayitNo.setter
    def kayitNo(self,value):
        self._kayitNo=value
    @property
    def sayfaSayisi(self):
        return self._sayfaSayisi
    @sayfaSayisi.setter
    def sayfaSayisi(self,value):
        self._sayfaSayisi=value
    @property
    def yayinTarihi(self):
        return self._yayinTarihi
    @yayinTarihi.setter
    def yayinTarihi(self,value):
        self._yayinTarihi=value
    @property
    def yayinEvi(self):
        return self._yayinEvi
    @yayinEvi.setter
    def yayinEvi(self,value):
        self._yayinEvi=value
    
class kitap(kaynak):
    def __init__(self,baslik,kayitNo,sayfaSayisi,yayinTarihi,yayinEvi,yazar,tür,baskiSayisi):
        super().__init__(baslik,kayitNo,sayfaSayisi,yayinTarihi,yayinEvi)
        self.yazar = yazar
        self.tür=tür
        self.baskiSayisi=baskiSayisi
    @property
    def yazar(self):
        return self._yazar
    @yazar.setter
    def yazar(self,value):
        self._yazar=value
    @property
    def tür(self):
        return self._tür
    @tür.setter
    def tür(self,value):
        self._tür=value
    @property
    def baskiSayisi(self):
        return self._baskiSayisi
    @baskiSayisi.setter
    def baskiSayisi(self,value):
        self._baskiSayisi=value
class dergi(kaynak):
    def __init__(self,baslik,kayitNo,sayfaSayisi,yayinTarihi,yayinEvi,sayiNo,editör):
        super().__init__(baslik,kayitNo,sayfaSayisi,yayinTarihi,yayinEvi)
        self.sayiNo=sayiNo
        self.editör=editör
    @property
    def sayiNo(self):
        return self._sayiNo
    @sayiNo.setter
    def sayiNo(self,value):
        self._sayiNo=value
    @property
    def editör(self):
        return self._editör
    @editör.setter
    def editör(self,value):
        self._editör=value
class islem(ABC):
    @abstractmethod
    def ekle(self):
        pass
    @abstractmethod
    def sil(self):
        pass
    @abstractmethod
    def guncelle(self):
        pass
    @abstractmethod
    def listele(self):
        pass
class kitapİslem(islem):
    def __init__(self):
        self.kitaplar=[]
    def ekle(self):
        print("--Kitap Ekleme--")
        baslik=input("Kitap başlığını giriniz:")
        yazar=input("Kitap yazarını giriniz:")
        tür=input("Kitap türünü giriniz:")
        baskiSayisi=int(input("Kitap baski sayısını giriniz:"))
        kayitNo=int(input("Kitap kayıt numarasını giriniz:"))
        sayfaSayisi=int(input("Kitap sayfa sayısını giriniz:"))
        yayinTarihi=input("kitap yayın tarihini giriniz:")
        yayinEvi=input("Kitap yayın evini giriniz:")
        yeniKitap=(kitap(baslik,kayitNo,sayfaSayisi,yayinTarihi,yayinEvi,yazar,tür,baskiSayisi))
        self.kitaplar.append(yeniKitap)
    def sil(self):
        print("--Kitap silme İşlemi--")
        KayitNo=int(input("silmek istediğiniz kitabın kayıt numarasını giriniz: "))
        for i in self.kitaplar:
            if i.kayitNo==KayitNo:
                print("kayıt bulundu")
                self.kitaplar.remove(i)
                print(f"{i.baslik} adlı kitap silindi.")
    def guncelle(self):
        print("---Kitap güncelleme işlemi---")
        KayitNo=input("Değişiklik yapmak istediğiniz kitabın kayıt numarasını giriniz:")
        for i in self.kitaplar:
            if i.kayitNo==KayitNo:
                print("1.kitap başlığını güncelle")
                print("2.kitap yazarını güncelle")
                print("3.kitap türünü güncelle")
                print("4.kitabın baskı sayısını güncelle")
                print("5.kitabın sayfa sayısını güncelle")
                print("6.kitabın yayın tarihini güncelle")
                print("7.kitabın yayın evini güncelle")
                print("8. iptal")
                secim=input("yapmak istediğiniz işlemi giriniz:(1/9)")
                if secim=='1':
                    yeni_baslik=input("kitabın yeni başlığı: ")
                    i.baslik=yeni_baslik
                    print(f'kitabın basliği {i.baslik} olarak güncellendi')
                if secim=='2':
                    yeni_yazar=input("Kitabın yeni yazar adını giriniz: ")
                    i.yazar=yeni_yazar
                    print(f'Kitabın yazar adı {i.yazar} olarak güncellendi')
                if secim=='3':
                    yeni_tür=input("Kitabın yeni türü: ")   
                    i.tür=yeni_tür
                    print(f'Kitabın türü {i.tür} olarak güncellendi')
                if secim=='4':
                    yeni_baski=input("Kitabın yeni baski sayisini giriniz: ")
                    i.baskiSayisi=yeni_baski
                    print(f'Kitabın baskı sayısı {i.baskiSayisi} olarak güncellendi')
                if secim=='5':
                    yeni_sayfasayisi=input("Kitabın yeni sayfa sayısını giriniz: ")
                    i.sayfaSayisi=yeni_sayfasayisi
                    print(f'Kitabın sayfa sayısı {i.sayfaSayisi} olarak güncellendi')
                if secim=='6':
                    yeni_yayintarihi=input("Kitabın yeni yayın tarihini giriniz: ")
                    i.yayinTarihi=yeni_yayintarihi
                    print(f'Kitabın yayın tarihi {i.yayinTarihi} olarak güncellendi')
                if secim=='7':
                    yeni_yayinevi=input("Kitabın yeni yayınevini giriniz:")
                    i.yayinEvi=yeni_yayinevi
                    print(f'Kitabın yayınevi {i.yayinEvi} olarak güncellendi')
                if secim=='8':
                    print("Çıkılıyor....")
                    break
            else:
                print(f'{KayitNo} kayıt numarasına sahip kitap yoktur!!!')
    def  listele(self):
        if self.kitaplar==None:
            print("Kayıt bulunamadı (kütüphanede hiç kitap verisi bulunmuyor)")
        print("----Kitap listesi-------")
        for i in self.kitaplar:
            print(f'{i}. kitabın başlığı:{i.baslik}, kitabın yazarı:{i.yazar}, kitabın türü:{i.tür}, kitabın baskı sayısı:{i.baskiSayisi}, kitabın sayfa sayısı:{i.sayfaSayisi}, kitabın yayın tarihi:{i.yayinTarihi}, kitabın yayınevi:{i.yayinEvi} ')  
            print(f'Kütüphanedeki toplam kitap sayısı:{len(self.kitaplar)}')
class dergiİslem(islem):
    def __init__(self):
        self.dergiler=[]
    def ekle(self):
        print("---Dergi ekleme işlemi---")
        baslik=input("Derginin başlığını giriniz: ")
        kayitNo=input("Derginin kayıt numarasını giriniz: ")
        sayfaSayisi=input("Derginin sayfa sayısını giriniz: ")
        yayinTarihi=input("Derginin yayın tarihini giriniz: ")
        yayinEvi=input("Derginin yayınevini giriniz:")
        sayiNo=input("Derginin sayı numarasını giriniz: ")
        editör=input("Derginin editörünü giriniz: ")
        yeni_dergi=(dergi(baslik,kayitNo,sayfaSayisi,yayinTarihi,yayinEvi,sayiNo,editör))
        self.dergiler.append(yeni_dergi)
    def sil(self):
        print("---Dergi silme işlemi---")
        skayitNo=input("Silmek istediğiniz derginin kayıt numarasını giriniz: ")
        for i in self.dergiler:
          if i.kayitNo==skayitNo:
              print("kayıt bulundu")
              self.dergiler.remove(i)
              print(f'{i.baslik} adlı dergi silindi ')
          else:
              print(f'{skayitNo} kayıt numaralı dergi bulunamadı')
    def guncelle(self):
        print("---Dergi güncelleme işlemi---")
        KayitNo=input("Değişiklik yapmak istediğiniz derginin kayıt numarasını giriniz:")
        for i in self.kitaplar:
            if i.kayitNo==KayitNo:
                print("1.Derginin başlığını güncelle")
                print("2.Derginin kayıt numarasını güncelle")
                print("3.Derginin sayfa sayısını güncelle")
                print("4.Derginin yayın tarihini güncelle")
                print("5.Derginin yayınevini güncelle")
                print("6.Derginin sayı numarasını güncelle")
                print("7.Derginin editörünü güncelle")
                print("8.çıkış")
                secim=input("yapmak istediğiniz işlemi giriniz:(1/8)")
                if secim=='1':
                    yeni_baslik=input("Derginin yeni başlığını giriniz:")
                    i.baslik=yeni_baslik
                    print(f'Derginin başlığı {i.baslik} olarak güncellendi')
                if secim=='2':
                    yeni_kayitno=input("Derginin yeni kayıt numarasını giriniz:")
                    i.kayitNo=yeni_kayitno
                    print(f'Derginin kayıt numarası {i.kayitNo} olarak güncellendi')
                if secim=='3':
                   yeni_sayfaSayisi=input("Derginin yeni sayfa sayısını giriniz: ")
                   i.sayfaSayisi=yeni_sayfaSayisi
                   print(f'Derginin sayfa sayısı {i.sayfaSayisi} olarak güncellendi')
                if secim=='4':
                    yeni_yayintarihi=input("Derginin yeni yayın tarihini giriniz: ")
                    i.yayinTarihi=yeni_yayintarihi
                    print(f'Derginin yayın tarihi {i.yayinTarihi} olarak güncellendi ')
                if secim=='5':
                    yeni_yayinevi=input("Derginin yeni yayınevini giriniz: ")
                    i.yayinEvi=yeni_yayinevi
                    print(f'Derginin yayınevi {i.yayinEvi} olarak güncellendi ')
                if secim=='6':
                    yeni_sayino=input("Derginin yeni sayı numarasını giriniz: ")
                    i.sayiNo=yeni_sayino
                    print(f'Dergin sayfa sayısı {i.sayfaSayisi} olarak güncellendi ')
                if secim=='7':
                    yeni_editör=input("Derginin yeni editörünü giriniz: ")
                    i.editör=yeni_editör
                    print(f'Derginin editörü {i.editör} olarak güncellendi ')
                if secim=='8':
                    print("çıkılıyor...")
                    break
    def listele(self):
        if self.dergiler==None:
            print("Kayıt bulunamadı (kütüphanede hiç dergi verileri bulunmuyor)")
        print("-----Dergilerin listesi------")
        for i in self.dergiler:
            print(f'{i}. Derginin başlığı:{i.baslik}, kayıt numarası:{i.kayitNo}, sayfa sayısı:{i.sayfaSayisi}, yayın tarihi:{i.yayinTarihi}, yayınevi:{i.yayinEvi}, sayı numarası:{i.sayiNo} editörü:{i.editör}')
        print(f'Kütüphanedeki toplam dergi sayısı:{len(self.dergiler)}')
kitap_islem=kitapİslem()
dergi_islem=dergiİslem()
while True:
       menu.goster()
       secim=input("Yapmak istediğiniz işlemi seçiniz:(1/9)")
       if secim=='1':
           kitap_islem.ekle()
       elif secim=='2':
           kitap_islem.sil()
       elif secim=='3':
           kitap_islem.guncelle()
       elif secim=='4':
           kitap_islem.listele()
       elif secim=='5':
           dergi_islem.ekle()
       elif secim=='6':
           dergi_islem.sil()
       elif secim=='7':
           dergi_islem.guncelle()
       elif secim=='8':
           dergi_islem.listele()
       elif secim=='9':
           print("programdan çıkılıyor.....")
           break
       else:
           print("Lütfen geçerli işlem seçiniz!")