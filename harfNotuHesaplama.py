# vize %40 , final %60 etkilidir.


vize=int(input("Vize notu:"))
final=int(input("Final notu:"))
ortalama=vize*40/100 + final*60/100

if ortalama<50:
    print("Harf notu:FF","\nOrtalamaniz:",ortalama)
    
elif ortalama>=50 and ortalama<55:
    print("Harf notu:DD","\nOrtalamaniz:",ortalama)
    
elif ortalama>=55 and ortalama<=59:
    print("Harf notu:DC","\nOrtalamaniz:",ortalama)

elif ortalama>59 and ortalama<=64:
    print("Harf notu:CC","\nOrtalamaniz:",ortalama)

elif ortalama>=65 and ortalama<=69:
    print("Harf notu:CB","\nOrtalamaniz:",ortalama)

elif ortalama>=70 and ortalama<=79:
    print("Harf notu:BB","\nOrtalamaniz:",ortalama)
    
elif ortalama>=80 and ortalama<=89:
    print("Harf notu:BA""\nOrtalamaniz:",ortalama)

elif ortalama>=90 and ortalama<=100:
    print("Harf notu:AA", "\nOrtalamaniz:",ortalama)


