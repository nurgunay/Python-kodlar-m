#ic acilarina gore ucgen cesidi bulan program. 

print("Üçgenin iç açı ölcülerini giriniz")

ucgenAci=int(input("Birinci iç açı ölçüsü:"))
ucgenAci2=int(input("İkinci iç açı ölçüsü:"))
ucgenAci3=int(input("Üçüncü iç açı ölçüsü:"))
   
icAciToplami= ucgenAci + ucgenAci2 + ucgenAci3
   
if icAciToplami==180:
    if ucgenAci==60 and ucgenAci2==60:
        print("\n--> Bu bir eşkenar üçgendir.\n")
        
        
    elif (ucgenAci==ucgenAci2 or ucgenAci==ucgenAci3 or ucgenAci3==ucgenAci2):
        print("\n--> Bu bir ikizkenar üçgendir.\n")
        
        
    elif ucgenAci != ucgenAci2 and ucgenAci2 != ucgenAci3:
        print("\n--> Bu bir çeşitkenar üçgendir.")
        
        
else:
    print("Girdiğiniz değerlerin toplamı 180 olmamaktadır.")

