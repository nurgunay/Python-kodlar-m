""" KULLANICIYA SİNEMA YA DA TİYATRO TERCİHİ SORULSUN. SİNEMA İZLEMEK İÇİN 20 TL TİYATRO İÇİN 15 TL ÖDENMESİ GEREKMEKTEDİR. ÖĞRENCİLERE
 % 50 İNDİRİM YAPILMAKTADIR. ÖĞRENCİ OLMAYANLARA NORMAL TUTAR UYGULANMAKTADIR."""
    
# sinema mı tiyatro mu?

tercih = input("- Sinema bileti mi almak istersiniz, tiyatro bileti mi? (S-T):")

sinema = 20
tiyatro = 15
kisi=input("- Öğrenci misiniz? (E/H):")


while True:
    #tercih sinema ise iki ayrı degisken tanimlandi. Ogrenciler icin indirimli tutar kullanilir.
    if tercih == 'S':
        indirimsiz = sinema
        indirimli = sinema - (sinema/2)
        
        #ogrenci misiniz testi Evet ise indirimli tutarı uygular. H ise indirimsiz tutar uygulanır ve yazdirilir.
        if kisi == "E":
            print("- Toplam tutar:",indirimli,"TL")
        else:
            print("- Toplam tutar:",indirimsiz,"TL")
        break
    
    #tercih tiyatro ise indirimli ve indirimsiz olarak iki farkli degisken kullanilir.
    if tercih == "T":
        indirimsiz = tiyatro
        indirimli = tiyatro - (tiyatro/2)
        
        # ogrenci misiniz testi sonucu E ise indirimli tutar, H ise indirimsiz tutar uygulanır ve yazdirilir.
        if kisi == "E":
            print("- Toplam tutar:",indirimli,"TL")
        else:
            print("- Toplam tutar:",indirimsiz,"TL")
        break
