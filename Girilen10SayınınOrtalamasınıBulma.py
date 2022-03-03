#kullanıcıdan alınan 10 sayının toplamını ve ortalamasını bulan program

toplam = 0
ortalama = 0

for i in range(10):
    sayı = int(input("Sayı giriniz: "))
    toplam += sayı

ortalama = toplam/10

print("\n--> Sayıların Toplamı = ",toplam,"\n")
print("--> Sayıların Ortalaması = ",ortalama)
    
 