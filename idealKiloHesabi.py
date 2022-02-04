# IDEAL KİLO  HESAPLAMA

from math import pow

kilo=int(input("Kilonuz(kg):"))
boy=float(input("Boyunuz(metre cinsinden):"))

#vki: vucut kitle indeksi
vki=kilo/(boy*boy)

if (vki<=18.5):
    print("--> Düşük Kilolu",vki)

elif (vki>18.5 and vki<=24.9):
    print("--> Normal Kilolu",vki)
    
elif (vki>24.9 and vki<=29.9):
    print("--> Fazla Kilolu",vki)
    
elif (vki>29.9 and vki<=40):
    print("--> Obez",vki)
    
elif (vki>40):
    print("--> Aşırı Obez",vki)
