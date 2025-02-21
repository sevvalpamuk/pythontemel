faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)

faiz = str(faiz)
print(type(faiz))

vade = int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))

vade = vade + 12

print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))

# Listeler
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))
print(krediler[0])
print(len(krediler))

dizi = ["İhtiyaç Kredisi", 10, 5.2]
print(dizi)

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop()
print(krediler)

# Döngüler
for i in range(5, 11):
    print(i)

print("*****************")

for i in range(0, 51, 10):
    print(i)

print("*****************")

for kredi in krediler:
    print(kredi)

print("*****************")

for i in range(len(krediler)):
    print(krediler[i])

print("*****************")

# Sonsuz Döngü
# while True:
#     print("Bu bir sonsuz döngüdür.")

i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("*****************")

i = 0
while i < len(krediler):
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break
    i += 1

print("***** Son Döngü *****")

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
i = 0
while i < len(krediler):
    print(i)
    print(krediler[i])
    i += 1
    if krediler[i] == "Konut Kredisi":
        break
indirim = 20

# Fonksiyon Tanımlama
def calculate():
    print(100 - 20)

def calculateWithParams(fiyat, indirim):
    print(fiyat - indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50, 10)
calculateWithParams(100, 30)

sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")

def calculateAndReturn(fiyat, indirim):
    return fiyat - indirim

yeniFiyat = calculateAndReturn(200, 50)
print(yeniFiyat)

print(yeniFiyat + 10)

# Void fonksiyonlar ve return fonksiyonlar
def calculatePrice(price, discount):
    print(price - discount)

def calculatePriceAndReturn(price, discount):
    return price - discount

print("****************")

fonk1 = calculatePrice(100, 50)
fonk2 = calculatePriceAndReturn(300, 100)

print(f"159. satır: {fonk1 + 100}")
print(f"160. satır: {fonk2 + 100}")
