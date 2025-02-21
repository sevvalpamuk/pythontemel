print("Kodlamaio")

baslik = "Taşıt Kredisi"
print(baslik)

# string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)

# int, integer => tam sayı
vade = 36
vade2 = "36"

# float, decimal, double
aylikOdeme = 200.50

# bool, boolean => True veya False
yukselisteMi = False

# matematiksel operatörler
print(5 + 5)
print(vade + 12)
print(vade + 6)
print(36 + 6)
print(5 - 5)

# bölme işlemleri
print(5 / 5)
print(vade / 2)
print(vade / 2)
print(10 / 2)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# mod (kalan) operatörü
print(10 % 2)
print(vade % 5)
print(30 % 10)

# karşılaştırma operatörleri
print(1 == 2)
print(3 > 1)
print(1 > 1)
print(1 < 2)
print(1 <= 1)
print(1 != 1)
print(1 != 2)

# or ve and operatörleri
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)
print(1 > 2 and 5 > 2 and 3 > 2)

# karar yapıları (if-else)
sayil1 = 10
sayil2 = 15

if sayil1 > sayil2:
    print("Sayi 1 Sayı 2'den büyüktür")
    print("Hala if bloğunun içerisindeyim")

if sayil1 < sayil2:
    print("Sayi 1 Sayı 2'den küçüktür")
elif sayil1 == sayil2:
    print("İki sayı eşittir")
else:
    print("Sayi 1 Sayı 2'den büyüktür")

print("Burası if bloğunun dışıdır.")

# iç içe if yapısı
print("*****************")

if sayil1 <= sayil2:
    print("Sayi 1 Sayı 2'den küçüktür")
    if sayil1 == sayil2:
        print("İki sayı eşittir")
    else:
        print("Sayi 1 Sayı 2'den büyüktür")

print("Burası if bloğunun dışıdır.")
