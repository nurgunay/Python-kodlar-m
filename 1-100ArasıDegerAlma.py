# 1-100 arasında sayı girilmesi istenir.
# Girilen sayı aralık dışındaysa gerekli uyarı verilir.
# 1-100 arasında bir sayı girilene kadar sayı girişi alınmaya devam eder.


sayı = int(input("1-100 arasında bir sayı giriniz: "))
    
while True:
    
    if(sayı < 1):
        print("Tekrar deneyin. 1 ve 1'den büyük sayı girmelisiniz!")
        while(sayı < 1):
            sayı = int(input("1-100 arasında bir sayı giriniz: "))
        
    
    elif(sayı > 100):
        print("Tekrar deneyin. 100'den küçük bir sayı girmelisiniz!")
        while(sayı > 100):
            sayı = int(input("1-100 arasında bir sayı giriniz: "))
        
        
    elif(sayı >= 1 and sayı <= 100):
        print("Tebrikler. 1-100 arasında bir sayı girdiniz.")
        break
        