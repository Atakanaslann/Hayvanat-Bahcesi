from abc import ABC, abstractmethod
import datetime
from random import randint
import random
import tkinter as tk
from PIL.ImageTk import PhotoImage
import cv2 
from prettytable import PrettyTable

x = PrettyTable()

class Hayvanlar:
    def __init__(self,isim,yasi,cinsi,saglik,yeme,uyuma,hareketEtme,yetenek,olay):
        self.isim        = isim
        self.yasi        = yasi
        self.cinsi       = cinsi
        self.saglik      = saglik
        self.yeme        = yeme
        self.uyuma       = uyuma
        self.hareketEtme = hareketEtme
        self.yetenek     = yetenek
        self.olay        = olay

class Ziyaretciler:
    AileYaslıst     = [16,28,46,53,55,19,40,35,42,17,19,53,54,45]
    OgrencıYaslıst  = [18,22,19,7,9,12,15,13,17,11,13]
    BıreyselYaslıst = [16,19,22,25,46,43,32,51]
    def __init__(self,zYasi,grupTuru,yemleme,hayvanlarıIzleme,degisken = AileYaslıst,degısken2 = OgrencıYaslıst,degısken3 = BıreyselYaslıst):
        self.zYasi                = zYasi    
        self.grupTuru             = grupTuru
        self.grupTuru             = {"1" :"Aile","2":"Öğrenci","3":"Bireysel"}
        self.yemleme              = yemleme
        self.hayvanlarıIzleme     = hayvanlarıIzleme
        self.aileYasListesi       = degisken
        self.ogrenciYasListesi    = degısken2
        self.bireyselYasListesi   = degısken3
       
        
    def yasGrup(self):
        print("\nZiyaretçi Girişi Yapıldı\n")
        secim1 = str(input("\n1-Aile\n2-Öğrenci\n3-Bireysel\n\nGrup türünüzü seçiniz: "))
        if secim1 == "1":
            print("\nSeçiminiz : {}".format(self.grupTuru[secim1]))
            aileYas=int(input("\n{} Yaş Ortalaması: ".format(self.grupTuru[secim1])))
            self.aileYasListesi.append(aileYas)
      
        elif secim1 == "2":
            print("Seçiminiz : {}".format(self.grupTuru[secim1]))
            self.ogrenciYas=int(input("{} Yaş Ortalaması: ".format(self.grupTuru[secim1])))
            self.ogrenciYasListesi.append(self.ogrenciYas)          
            
        elif secim1 == "3":
            print("Seçiminiz : {}".format(self.grupTuru[secim1]))
            self.bireyselYas=int(input("{} Yaş Ortalaması: ".format(self.grupTuru[secim1])))
            self.bireyselYasListesi.append(self.bireyselYas)

    @staticmethod
    def hayvanEtkilesim(hayvan):
        x.field_names = ["Hayvan İsmi","Hayvan Cinsi", "Beslenme Şekli", "Sağlık Durumu", "Yaş","Uyku Saatleri","Hareket Hızı"]
        x.add_row([hayvan.isim, hayvan.cinsi, hayvan.yeme,hayvan.saglik,hayvan.yasi,hayvan.uyuma,hayvan.hareketEtme])
        print(x)
        #print("\n\n{} Hakkında Bilgiler\n\nCinsi: {}\nBeslenme türü: {}\nSağlık durumu: {}\nYaşı: {}\nUyku saati: {}\nHareket hızı: {}".format(hayvan.isim, hayvan.cinsi, hayvan.yeme,hayvan.saglik,hayvan.yasi,hayvan.uyuma,hayvan.hareketEtme))
        
        while True:
            etkilesim = input("""\n\n1-{} hayvanına yem at\n2-Hayvanla Etkileşime Gir\n3-Hayvan seçimine dön\n-->""".format(hayvan.isim))
            if etkilesim == "1":
                print("\n{} doymuş gözüküyor.".format(hayvan.isim))

            elif etkilesim == "2":
                kamera=cv2.VideoCapture('C:\\Users\\acer\\Desktop\\30günde js\\piton\\{}.gif'.format(hayvan.isim)) # oynatılacak videoyu tanımlama
                kamera.set(cv2.CAP_PROP_FRAME_WIDTH,640)
                kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,480) #­ Kamera Boyutlandırma
              
                while True:
                    ret,goruntu=kamera.read() # kamera okumayı başlatma

                    if not ret:
                        kamera.set(cv2.CAP_PROP_POS_FRAMES,0)
                        continue

                    cv2.imshow(f'{hayvan.isim}',goruntu) # görüntüyü gösterme

                    if cv2.waitKey(60) == ord('t'): # t tuşuna basılınca durdur.
                        break
                    
                kamera.release() # kamerayı serbest bırak.t
                cv2.destroyAllWindows() # açılan pencereleri kapat.
                break

            elif etkilesim == "3":
                break
            else:
                print("Hatalı giriş yaptınız.")


    @classmethod
    def Istatistik(cls):
        toplamKisi = len(cls.AileYaslıst) + len(cls.OgrencıYaslıst) +len(cls.BıreyselYaslıst)
        print("Anlık Ziyaretçi Sayısı: "+ str(toplamKisi))

    def PersonelIstatistik(self, aileToplam, ogrenciToplam, bireyselToplam):
        self.__aileToplam = aileToplam
        self.__ogrenciToplam = ogrenciToplam
        self.__bireyselToplam = bireyselToplam
    def getIstatistik(self):
        return self.__aileToplam, self.__ogrenciToplam, self.__bireyselToplam
    
    def setIstatistik(self, aileToplam, ogrenciToplam, bireyselToplam):
        self.__aileToplam = aileToplam
        self.__ogrenciToplam = ogrenciToplam
        self.__bireyselToplam = bireyselToplam
        


class Ortam(ABC):
    def __init__(self,bulunanHayvanlar):
        self.bulunanHayvanlar = bulunanHayvanlar
        self.bulunanHayvanlar = []

    @abstractmethod
    def kosullar(self):
        pass
                    
class Tropikal(Ortam):
    def __init__(self, bulunanHayvanlar):
        super().__init__(bulunanHayvanlar)
        self.bulunanHayvanlar=["",""]
        
    def kosullar(self):
        pencere = tk.Tk()
        pencere.title("Tropikal")
        pencere.geometry("1920x1080")
        pencere.resizable(width="TRUE", height="TRUE")
        simge1 = PhotoImage(file="C:\\Users\\acer\\Desktop\\30günde js\\piton\\tropikal2.jpg")
        düğme1=tk.Button(text="", image=simge1,font="Times 12 bold",bg="white",fg="white")  
        düğme1.place(relx=0.2,rely=0.1,width=1000,height=667)
        tk.mainloop()


class Kutup(Ortam):
    def __init__(self, bulunanHayvanlar):
        super().__init__(bulunanHayvanlar)
        self.bulunanHayvanlar=["",""]
        
    def kosullar(self):
        pencere = tk.Tk()
        pencere.title("Kutup")
        pencere.geometry("1000x596+50+100")
        pencere.resizable(width="TRUE", height="TRUE")
        simge1 = PhotoImage(file="C:\\Users\\acer\\Desktop\\30günde js\\piton\\kutup2.jpg")
        düğme1=tk.Button(text="", image=simge1,font="Times 12 bold",bg="white",fg="white")
        düğme1.place(relx=0.2,rely=0.1,width=1000,height=596)
        tk.mainloop()
        

class Savan(Ortam):
    def __init__(self, bulunanHayvanlar):
        super().__init__(bulunanHayvanlar)
        self.bulunanHayvanlar=["",""]
       
    def kosullar(self):
        pencere = tk.Tk()
        pencere.title("Savan")
        pencere.geometry("1624x1080")
        pencere.resizable(width="TRUE", height="TRUE")
        simge1 = PhotoImage(file="C:\\Users\\acer\\Desktop\\30günde js\\piton\\savan2.jpg")
        düğme1=tk.Button(text="", image=simge1,font="Times 12 bold",bg="white",fg="white")
        düğme1.place(relx=0,rely=0,width = 1624,height=1080)
        tk.mainloop()


class Memeli(Hayvanlar):
    def __init__(self, isim, yasi, cinsi, saglik, yeme, uyuma, hareketEtme, yetenek,olay):
        super().__init__(isim, yasi, cinsi, saglik, yeme, uyuma, hareketEtme, yetenek,olay)
class Balik(Hayvanlar):
    def __init__(self, isim, yasi, cinsi, saglik, yeme, uyuma, hareketEtme, yetenek,olay):
        super().__init__(isim, yasi, cinsi, saglik, yeme, uyuma, hareketEtme, yetenek,olay)
class Kus(Hayvanlar):
    def __init__(self, isim, yasi, cinsi, saglik, yeme, uyuma, hareketEtme, yetenek,olay):
        super().__init__(isim, yasi, cinsi, saglik, yeme, uyuma, hareketEtme, yetenek,olay)
class Surungen(Hayvanlar):
    def __init__(self, isim, yasi, cinsi, saglik, yeme, uyuma, hareketEtme, yetenek,olay):
        super().__init__(isim, yasi, cinsi, saglik, yeme, uyuma, hareketEtme, yetenek,olay)

    
kaplumbağa       = Surungen("Kaplumbağa", "1", "testudines", "Sağlıklı", "Otçul", "0-1", "Yavaş", "amfibik","C:\\Users\\acer\\Desktop\\30günde js\\piton\\kaplumbağa.gif")
Anakonda         = Surungen("Anakonda", "6", "Eunectes", "Sağlıklı", "Etçil", "Orta", "Su", "Su","C:\\Users\\acer\\Desktop\\30günde js\\piton\\anakonda.gif")
timsah           = Surungen("Timsah", "5", "niloticus", "Hasta", "Etçil", "2-3", "Yavaş", "amfibik","C:\\Users\\acer\\Desktop\\30günde js\\piton\\timsah.gif")#son madde dosya yolu olacack
maymun           = Memeli("Maymun", "8", "Cercopithecidae", "Sağlıklı", "Otçul", "Hızlı", "Ağaçlık Alanlar", "Canlı Doğurur","C:\\Users\\acer\\Desktop\\30günde js\\piton\\maymun.gif")
kanguru          = Memeli("Kanguru", "3", "macropus", "Sağlıklı", "Otçul", "3-4", "Hızlı", "kara","C:\\Users\\acer\\Desktop\\30günde js\\piton\\kanguru.gif")
Papağan          = Kus("Papağan", "4", "Psittacidae", "Sağlıklı", "Tohumlu Bitkiler", "Orta", "Kara", "Yüksek Uçan","C:\\Users\\acer\\Desktop\\30günde js\\piton\\papağan.gif")
kartal           = Kus("Kartal", "2", "aquila", "Sağlıklı", "Etçil", "1-2", "Hızlı", "hava","C:\\Users\\acer\\Desktop\\30günde js\\piton\\kartal.gif")
penguen          = Kus("Penguen", "1", "spheniscidae", "Sağlıklı", "Balıkçıl", "1-2", "Yavaş", "su","C:\\Users\\acer\\Desktop\\30günde js\\piton\\penguen.gif")
yunus            = Balik("Yunus","4","Tursiops","Hasta","Etçil","2-3","Hızlı","Yüzme","C:\\Users\\acer\\Desktop\\30günde js\\piton\\yunus.gif")
köpekbalığı      = Balik("Köpekbalığı","1","Carcharodon carcharias","Sağlıklı","Etçil","3-4","Hızlı","","C:\\Users\\acer\\Desktop\\30günde js\\piton\\kbalığı.gif")
caretta          = Balik("Caretta","3","Caretta caretta","Sağlıklı","Etçil","7-8","Yavaş","","C:\\Users\\acer\\Desktop\\30günde js\\piton\\caretta.gif")
aslan            = Memeli("Aslan","5","Panthera leo","Hasta","Etçil","5-6","Hızlı","","C:\\Users\\acer\\Desktop\\30günde js\\piton\\aslan.gif") 

hayvanListesi =[kaplumbağa,Anakonda,timsah,maymun,kanguru,Papağan,kartal,penguen,yunus,köpekbalığı,caretta,aslan]

                                           ###-----------ARAYÜZ--------------###

while True:
    ziyaretci = Ziyaretciler("","","","")
    print("\n\n------------Sanal Hayvanat Bahçesi Sümülasyonu'na Hoşgeldiniz------------\n\n\n")
    secim = int(input("1-Ziyaretçi Girişi\n2-Personel Girişi\n3-Çıkış Yap\n--> "))
    if secim == 1:

    # yasGrup() metodunu çağırın
        ziyaretci.yasGrup()

    # Istatistik() metodunu çağırın
        while True:
            zaman = datetime.datetime.now().hour
            hayvansecim = " "
            bolumSec = int(input("\n\n1-Hayvanat Bahçesini Gez\n2-Ortamlar Hakkında Bilgi Al\n3-İstatistikler\n4-Üst Menüye Dön\n-->"))
            
            if bolumSec == 1:
                kategorisecim = int(input("\nZiyaret etmek istediğiniz hayvan kategorisini seçiniz\n\n1-Sürüngen\n2-Kuş\n3-Balık\n4-Memeli\n5-Geri Dön\n-->"))
                
                while True:
                    
                    if kategorisecim == 1:
                        hayvansecim = str(input("\nZiyaret etmek istediğiniz hayvanı seçiniz\n\n1-Timsah\n2-Kaplumbağa\n3-Anakonda\n4-Çıkış\n-->"))
                       
                        if hayvansecim == "timsah":
                            hayvansecim = timsah
                            timsahDoluluk = random.randint(3,10)
                           
                            
                            if 9<=zaman<24:
                               
                                if timsahDoluluk <= 8:
                                    print("\n\nTimsah doluluk oranı %" + str(timsahDoluluk*10) + " girebilirsiniz.")
                                    ziyaretci.hayvanEtkilesim(hayvansecim)
                                
                                else:
                                    print("\n\nTimsah doluluk oranı %"+str(timsahDoluluk*10) + " şuanda giriş yapamazsınız.")
                                    break
                            else:
                                print("\n\nBu zaman aralığında bu hayvanı ziyaret edemezsiniz.")
                                break
                            
                        elif hayvansecim == "kaplumbağa":
                            hayvansecim = kaplumbağa
                            kaplumbagaDoluluk = random.randint(3,10)
                            
                            if 0<=zaman<17:
                                if kaplumbagaDoluluk <= 8:
                                    print("\n\nKaplumbağa doluluk oranı %" + str(kaplumbagaDoluluk*10) + " girebilirsiniz.")
                                    ziyaretci.hayvanEtkilesim(hayvansecim)
                                else:
                                    print("\n\nKaplumbağa doluluk oranı %"+str(kaplumbagaDoluluk*10) + " şuanda giriş yapamazsınız.")
                                    break
                            else:
                                print("\n\nBu zaman aralığında bu hayvanı ziyaret edemezsiniz.")
                                break
                            
                        
                        elif hayvansecim == "anakonda":
                            hayvansecim = Anakonda
                            anakondaDoluluk = random.randint(3,10)
                            
                            if 10<=zaman<21:
                                if anakondaDoluluk <= 8:
                                    print("\n\nAnakonda doluluk oranı %" + str(anakondaDoluluk*10) + " girebilirsiniz.")
                                    ziyaretci.hayvanEtkilesim(hayvansecim)
                                else:
                                    print("\n\nAnakonda doluluk oranı %"+str(anakondaDoluluk*10) + " şuanda giriş yapamazsınız.")
                                    break
                            else:
                                print("\n\nBu zaman aralığında bu hayvanı ziyaret edemezsiniz.")
                                break


                        elif hayvansecim == "çıkış" or 4:
                            # Bir üst menüye dönme
                            break
                    elif kategorisecim == 2:
                        hayvansecim = str(input("\nZiyaret etmek istediğiniz hayvanı seçiniz\n1-Kartal\n2-Papağan\n3-Penguen\n4-Çıkış\n-->"))

                        if hayvansecim == "kartal":
                            hayvansecim = kartal
                            kartalDoluluk = random.randint(3,10)
                           
                            if 9<=zaman<18:
                                if kartalDoluluk <= 8:
                                    print("\n\nKartal doluluk oranı %" + str(kartalDoluluk*10) + " girebilirsiniz.")
                                    ziyaretci.hayvanEtkilesim(hayvansecim)
                                else:
                                    print("\n\nKartal doluluk oranı %"+str(kartalDoluluk*10) + " şuanda giriş yapamazsınız.")
                                    break
                            else:
                                print("\n\nBu zaman aralığında bu hayvanı ziyaret edemezsiniz.")
                                break
                        elif hayvansecim == "papağan":
                            hayvansecim = Papağan
                            papaganDoluluk = random.randint(3,10)
                           
                            if 9<=zaman<18:
                                if papaganDoluluk <= 8:
                                    print("\n\nPapağan doluluk oranı %" + str(papaganDoluluk*10) + " girebilirsiniz.")
                                    ziyaretci.hayvanEtkilesim(hayvansecim)
                                else:
                                    print("\n\nPapağan doluluk oranı %"+str(papaganDoluluk*10) + " şuanda giriş yapamazsınız.")
                                    break
                            else:
                                print("\n\nBu zaman aralığında bu hayvanı ziyaret edemezsiniz.")
                                break

                        elif hayvansecim == "penguen":
                            hayvansecim = penguen
                            PenguenDoluluk = random.randint(3,10)
                           
                            if 9<=zaman<18:
                                if PenguenDoluluk <= 8:
                                    print("\n\nPenguen doluluk oranı %" + str(PenguenDoluluk*10) + " girebilirsiniz.")
                                    ziyaretci.hayvanEtkilesim(hayvansecim)
                                else:
                                    print("\n\nPenguen doluluk oranı %"+str(PenguenDoluluk*10) + " şuanda giriş yapamazsınız.")
                                    break
                            else:
                                print("\n\nBu zaman aralığında bu hayvanı ziyaret edemezsiniz.")
                                break

                        elif hayvansecim == "çıkış" or 4:
                            # Bir üst menüye dönme
                            break
                    elif kategorisecim == 3:
                        hayvansecim = str(input("\nziyaret etmek istediğiniz Hayvanı seçiniz\n 1 - Altın Balığı\n 2 - Vatoz\n 3 - Zebra Cichlid\n 4 - Mandarin Balığı\n 5 - Discus Balığı\n 6 - Denizatı\n 7 - Balina\n 8 - Kategori Seçimine Dön \n"))

                        if hayvansecim == "yunus":
                            hayvansecim = yunus
                            yunusDoluluk = random.randint(3,10)
                           
                            if 9<=zaman<18:
                                if yunusDoluluk <= 8:
                                    print("\n\nYunus doluluk oranı %" + str(yunusDoluluk*10) + " girebilirsiniz.")
                                    ziyaretci.hayvanEtkilesim(hayvansecim)
                                else:
                                    print("\n\nYunus doluluk oranı %"+str(yunusDoluluk*10) + " şuanda giriş yapamazsınız.")
                                    break
                            else:
                                print("\n\nBu zaman aralığında bu hayvanı ziyaret edemezsiniz.")
                                break
                        elif hayvansecim == "köpek balığı":
                            hayvansecim = köpekbalığı
                            kbalıkDoluluk = random.randint(3,10)
                          
                            if 9<=zaman<18:
                                if kbalıkDoluluk <= 8:
                                    print("\n\bKöpek Balığı doluluk oranı %" + str(kbalıkDoluluk*10) + " girebilirsiniz.")
                                    ziyaretci.hayvanEtkilesim(hayvansecim)
                                else:
                                    print("\n\nKöpek Balığı doluluk oranı %"+str(kbalıkDoluluk*10) + " şuanda giriş yapamazsınız.")
                                    break
                            else:
                                print("\n\nBu zaman aralığında bu hayvanı ziyaret edemezsiniz.")
                                break

                        elif hayvansecim == "caretta":
                            hayvansecim = caretta
                            carettaDoluluk = random.randint(3,10)
                            
                            if 9<=zaman<18:
                                if carettaDoluluk <= 8:
                                    print("\n\nCaretta Caretta doluluk oranı %" + str(carettaDoluluk*10) + " girebilirsiniz.")
                                    ziyaretci.hayvanEtkilesim(hayvansecim)
                                else:
                                    print("\n\nCAretta Caretta doluluk oranı %"+str(carettaDoluluk*10) + " şuanda giriş yapamazsınız.")
                                    break
                            else:
                                print("\n\nBu zaman aralığında bu hayvanı ziyaret edemezsiniz.")
                                break

                        elif hayvansecim == "çıkış" or 4:
                            # Bir üst menüye dönme
                            break
                    elif kategorisecim == 4:
                        hayvansecim = str(input("\nziyaret etmek istediğiniz Hayvanı seçiniz\n 1 - Kanguru\n 2 - Zürafa\n 3 - Maymun\n 4 - Fil\n 5 - Kaplan\n 6 - Kategori Seçimine Dön\n"))

                        if hayvansecim == "maymun":
                            hayvansecim = maymun
                            maymunDoluluk = random.randint(3,10)
                           
                            if 9<=zaman<18:
                                if maymunDoluluk <= 8:
                                    print("\n\nMaymun doluluk oranı %" + str(maymunDoluluk*10) + " girebilirsiniz.")
                                    ziyaretci.hayvanEtkilesim(hayvansecim)
                                else:
                                    print("\n\nMaymun doluluk oranı %"+str(maymunDoluluk*10) + " şuanda giriş yapamazsınız.")
                                    break
                                
                        elif hayvansecim == "aslan":
                            hayvansecim = aslan
                            aslanDoluluk = random.randint(3,10)
                           
                            if 9<=zaman<18:
                                if aslanDoluluk <= 8:
                                    print("\n\nAslan doluluk oranı %" + str(aslanDoluluk*10) + " girebilirsiniz.")
                                    ziyaretci.hayvanEtkilesim(hayvansecim)
                                else:
                                    print("\n\nAslan doluluk oranı %"+str(aslanDoluluk*10) + " şuanda giriş yapamazsınız.")
                                    break

                        elif hayvansecim == "kanguru":
                            hayvansecim = kanguru
                            kanguruDoluluk = random.randint(3,10)
                          
                            if 9<=zaman<18:
                                if kanguruDoluluk <= 8:
                                    print("\n\nYunus doluluk oranı %" + str(kanguruDoluluk*10) + " girebilirsiniz.")
                                    ziyaretci.hayvanEtkilesim(hayvansecim)
                                else:
                                    print("\n\nYunus doluluk oranı %"+str(kanguruDoluluk*10) + " şuanda giriş yapamazsınız.")

                        elif hayvansecim == "çıkış" or 4:
                            # Bir üst menüye dönme
                            break
                    elif kategorisecim == 5:
                        break
                    else:
                        print("Hatalı tuşlama yaptınız ")
                        break
            elif bolumSec == 2:
                ortamgor = int(input("\n\n1-Tropikal Ortamı\n2-Savan Ortamı\n3-Kutup Ortamı\n4-Geri Dön\n\nGitmek istediğiniz ortamı seçiniz\n-->"))
                if ortamgor == 1:
                    o1 = Tropikal("")
                    o1.kosullar()
                elif ortamgor == 2:
                    o1 = Savan("")
                    o1.kosullar()
                elif ortamgor == 3:
                    o1 = Kutup("")
                    o1.kosullar()
                elif ortamgor == 4:
                    break
                else:
                    print("Hatalı Tuşlama yaptınız")
            elif bolumSec == 3:
                ziyaretci.Istatistik()       # personel girişinde gözükecek (kapsülleme)

                #istatistikler
            elif bolumSec == 4:
                break
                

    elif secim == 2:
        sifre = 535519
        secim2 = int(input("\nPersonel Girişi İçin Şifrenizi Giriniz: "))
        if secim2==sifre:
            gorevSecim=int(input("\n1-Hayvan Yem Değiştir\n2-Çevreyi Temizle\n3-İstatistik\n4-TÜm Hayvanları GÖster\n5-Çıkış"))
            yem = 0
            temizleme=0
            if gorevSecim==1 and yem == 0 :
                print("Bütün hayvanlara yem verildi.")
                yem += 1               

            elif gorevSecim==1 and yem == 1:
                print("Bütün yemler taze.")

            elif gorevSecim==2 and temizleme==0:
                print("Çevre temizliği yapıldı.")
                
            elif gorevSecim==2 and temizleme==1:
                print("Hayvanat bahçesi temiz.")
            elif gorevSecim==3:
                ornek = Ziyaretciler("","","","","","","")
                ornek.setIstatistik("Aktif Aile: "+str(len(ornek.AileYaslıst)),"Aktif Öğrenci: "+str(len(ornek.OgrencıYaslıst)),"Aktif Bireysel: "+str(len(ornek.BıreyselYaslıst)))
                print(ornek.getIstatistik())
                elemanlar = {
                  "A" : {
                    "değer" : len(ziyaretci.aileYasListesi),
                    "renk" : "#FFA500",
                    "buton": "Aile",
                    "durum" : True
                  },
                  "B" : {
                    "değer" : len(ziyaretci.ogrenciYasListesi),
                    "renk" : "#E75480",
                    "buton": "Öğrenci",
                    "durum" : True
                  },
                  "C" : {
                    "değer" : len(ziyaretci.bireyselYasListesi),
                    "renk" : "#66FF00",
                    "buton": "Bireysel",
                    "durum" : True
                  },
                
                }
                

                degerler = [t["değer"] for t in elemanlar.values()]
                arayuz = tk.Tk()
                ekran_olcek = 0.6  # boyut için
                ekran_gen = int(arayuz.winfo_screenwidth() * ekran_olcek)
                ekran_yuk = int(arayuz.winfo_screenheight() * ekran_olcek)
                ekran_boyutu = str(ekran_gen)+'x'+str(ekran_yuk)
                arayuz.geometry(ekran_boyutu)
                arayuz.title("Pasta Grafiği")
                arayuz.resizable(False, False)
                canvas = tk.Canvas(arayuz, width=ekran_gen, height=ekran_yuk, background="white smoke")
                canvas.pack(expand=0)
                def pasta_dilimi(elemanlar, degerler):
                    grafik = int(ekran_yuk / 6)
                    buton_x = ((ekran_gen - ekran_yuk) / 2) + ekran_yuk
                    buton_y = ekran_yuk / (2 * (len(elemanlar) + 1))
                    bas = 0
                    for i, j in elemanlar.items():
                        aciklik = (j["değer"] / sum(degerler)) * 360
                        if j['durum'] is True:
                            canvas.create_arc(grafik, grafik, grafik * 5, grafik * 5, start=bas, extent=aciklik,fill=j["renk"], width=2)
                        
                        bas += aciklik
                pasta_dilimi(elemanlar, degerler)
                arayuz.mainloop()
                

            elif gorevSecim==4:
                x.field_names = ["Hayvan İsmi","Hayvan Cinsi", "Beslenme Şekli", "Sağlık Durumu", "Yaş","Uyku Saatleri","Hareket Hızı"]
                for i in hayvanListesi:
                    x.add_row([i.isim, i.cinsi, i.yeme,i.saglik,i.yasi,i.uyuma,i.hareketEtme],divider=True)
                print(x)


            elif gorevSecim==5:

                pass
                                              
            else:
                print("Hatalı Tuşlama Yaptınız.")
                break
            

        