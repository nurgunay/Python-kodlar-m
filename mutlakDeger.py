# girilen sayının mutlak değerini bulan program

sayı = int(input("Mutlak değerini bulmak istediğiniz sayıyı giriniz:"))

if (sayı > 0):
    print(sayı,"sayısının mutlak değeri: ",sayı)
   
elif (sayı == 0):
    print(sayı,"sayısının mutlak değeri: ",sayı)
    
else:
    print(sayı,"sayısının mutlak değeri: ",(sayı*(-1)))
    
