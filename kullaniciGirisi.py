#kullanıcı girişi doğrulama
import time 

print(""" 
***********************************
***** Kullanıcı Girişi Ekranı *****
***********************************
""")
      
SystemUsername = "AdminGiriş"
SystemPasswd = "0AdminParola0"
giriş_hakkı = 3
        
while True: 
    
    kullanıcıAdı= input("Kullanıcı Adı: ")
    parola= input("Parola: ")
    

    if (SystemUsername != kullanıcıAdı and SystemPasswd == parola):
        print("Kullanıcı Adı Hatalı \n")
        giriş_hakkı -= 1
    
    elif (SystemPasswd != parola and SystemUsername == kullanıcıAdı):
        print("Parola Hatalı \n")
        giriş_hakkı -= 1 
    
    elif(SystemUsername != kullanıcıAdı and SystemPasswd != parola):
        print("Kullanıcı Adı ve Parola Hatalı \n")
        giriş_hakkı -= 1
        
    else:
        print("Sisteme Başarıyla Giriş Yaptınız.\n")
        giriş_hakkı -= 1
        time.sleep(2) #biraz süre geçmesi için yazılan fonksiyon(time kütüphanesi, sleep fonks.)
        break
     
    if (giriş_hakkı == 0):
            print("Giriş Hakkınız Geçici Olarak Kısıtlandı\n10 Dakika Sonra Tekrar Deneyiniz.\nYönlendiriliyor...")
            time.sleep(2)
    
       
    
        

