isim = input("Adınızı soyadınızı giriniz :\n")
duzey = input("Hastalık düzeyini giriniz : (Hafif = (h) Orta = (o) Ağır = (a)\n")
prog = 1

if duzey == "h" or duzey == "o":
    kanama = int(input("Bir ayda meydana gelen ortalama kanamayı yazınız :\n"))
    if kanama < 4:
        prog = 0
    else:
        prog = 1
if prog :
    print("Programa alınacak")
    doktor_f8 = int(input("Doktorun önerdiği günlük faktör-8 miktarını giriniz :\n"))

    aylik_f8 = 12 * doktor_f8
    ucret = aylik_f8 * 1.25
    yesil = input("Hastanın yeşil kartı varmı ? (e/h)\n")

    if yesil == "e" :
        sgk = ucret + (ucret * 0.01)
    else:
        sgk = ucret + (ucret * 0.08)

    print("Sayın :",isim,"\n")
    print("Almanız gereken faktör-8 miktarı (Aylık) :", aylik_f8,"\n")
    print("SGK ya ödemeniz gereken aylık ücret : ",sgk,"TL\n")
else:
    print("Programa alınmayacak")