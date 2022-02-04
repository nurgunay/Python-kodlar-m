import random

secenek=["taş","kağıt","makas","çıkış"]
taş=secenek[0]
kağıt=secenek[1]
makas=secenek[2]
çıkış=secenek[3]


print("--- TAŞ KAĞIT MAKAS OYUNUNA HOŞ GELDİNİZ ---\n")

while (True):
    
    secim=int(input("1.Taş\n2.Kağıt\n3.Makas\n4.Oyundan Çıkış\nSeçiminizi giriniz: "))
    bil_secim=random.choice(secenek)


    if secim==1:
        
      if bil_secim==taş:
        print("\n--> Bilgisayarın secimi: Taş\n\n--> Sonuç: Berabere\n ")
        
      elif bil_secim==kağıt:
        print("\n--> Bilgisayarın secimi: Kağıt\n\n--> Sonuç: Kaybettiniz\n ")
        
      else:
        print("\n--> Bilgisayarın secimi: Makas\n\n--> Sonuç: Kazandınız\n ")
    
        
            
    if secim==2:
      if bil_secim==taş:
        print("\n--> Bilgisayarın secimi: Taş\n\n--> Sonuç: Kazandınız\n")
        
      elif bil_secim==kağıt:
        print("\n--> Bİlgisayarın secimi: Kağıt\n\n--> Sonuç: Berabere\n")
        
      else:
        print("\n--> Bilgisayarın secimi: Makas\n\n--> Sonuç: Kaybettiniz\n")
       
            
            
    if secim==3:
      if bil_secim==taş:
        print("\n--> Bilgisayarın secimi: Taş\n\n--> Sonuç: Kaybettiniz\n")
        
      elif bil_secim==kağıt:
        print("\n--> Bilgisayarın secimi: Kağıt\n\n--> Sonuç: Kazandınız\n ")
       
      else:
        print("\n--> Bilgisayarın secimi: Makas\n\n--> Sonuç: Berabere\n ")
  
  
  
    if secim==4:
      print("Oyundan çıkılıyor...")
      break


