
# ikinci dereceden denklem koklerini bulan program.
from math import sqrt 

print("- Ikinci Dereceden Denklem Koku Bulma -\n")

#kullanicidan a,b,c, ve x degerleri aliniyor.
a=int(input("- a degerini girin:"))
b=int(input("- b degerini girin:"))
c=int(input("- c degerini girin:"))
x=int(input("- x degerini girin:"))

#ikinci dereceden denklem formulu, delta formulu.
denklem=a*pow(x,2)+(b*x) +c
delta=pow(b,2)-(4*a*c)


#delta ile kok bulmak isteniyorsa, a ve b ve c degerleri sifir olamaz if kosulu ile kontrol ediliyor.
if a!=0 and b!=0 and c!=0:
    
    
    #a,b,c degerleri sifir degilse yeni bir if kosulu olusturulup deltanin durumu kontrol ediliyor.
    #delta<0 durumu kontrolu 
    if delta<0:
        print("\nDelta=",delta)
        print("Denklemin gercek koku yoktur.")
    
    
    #delta=0 durumu kontrolu
    elif delta==0:
        print("\nDelta=",delta)
        print("Denklemin cakisik iki koku vardir.")
        x1=-b / (2*a)
        x2=x1
        print("Kok 1 ve Kok 2:",int(x1))
    
    
    #delta>0 durumu kontrolu 
    else:
        print("\nDelta=",delta)
        print("Denklemin gercek iki koku vardir.")
        x1=-b + (sqrt(delta)/2*a)
        x2=-b - (sqrt(delta)/2*a)
        print("Kok 1:",int(x1), "\tKok 2:",int(x2))
        
        
#a,b,c sayilarinin sifir olma durumunda asagidaki adim gerceklesir ve islem sonlanir.      
else:
    print("Girilen degerler sifira esit olamaz!")


