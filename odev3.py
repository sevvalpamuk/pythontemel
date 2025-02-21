# Veri Tipleri ve Dönüşümler
faiz = 1.59
vade = "36"
kredi_adi = "İhtiyaç Kredisi"

print(type(faiz))      # <class 'float'>
print(type(vade))      # <class 'str'>
print(type(kredi_adi)) # <class 'str'>

print(int(vade) + 12)  # Stringi integer'a çevirip işlem yapma

faiz = str(faiz)       # Float'ı string'e çevirme
print(type(faiz))      # <class 'str'>

vade = int(input("Lütfen istediğiniz vade sayısını giriniz: "))  # Kullanıcıdan giriş alma
print(type(vade))
vade += 12

# String Interpolation (Metin İçinde Değişken Kullanımı)
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

# Listeler
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))  # <class 'list'>
print(krediler[0])     # Listenin ilk elemanı
print(len(krediler))   # Listenin uzunluğu

# Listeye Eleman Ekleme ve Çıkarma
krediler.append("Özel Kredi")
krediler.append("X Kredisi")
print(krediler)

krediler.pop()  # Son elemanı çıkar
print(krediler)

# Döngüler
for kredi in krediler:
    print(kredi)

for i in range(len(krediler)):
    print(krediler[i])

# While Döngüsü
i = 0
while i < len(krediler):
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break  # "Konut Kredisi"ni gördüğünde döngüyü sonlandır
    i += 1

# Fonksiyonlar
def calculate():
    print(100 - 20)

def calculate_with_params(fiyat, indirim):
    print(fiyat - indirim)

calculate()
calculate_with_params(50, 10)
calculate_with_params(100, 30)

def say_hello(name):
    print(f"Merhaba {name}")

say_hello("Halit")
say_hello("Arif")
say_hello("Mevlüt")

# Return Kullanımı
def calculate_and_return(fiyat, indirim):
    return fiyat - indirim

yeni_fiyat = calculate_and_return(200, 50)
print(yeni_fiyat)

# Nesne Yönelimli Programlama (OOP) - Class Kullanımı
class Human:
    # Constructor (Başlatıcı Metot)
    def __init__(self, name):
        self.name = name
        print("Bir human instance'i üretildi")

    def talk(self, sentence):
        print(f"{self.name}: {sentence}")

    def walk(self):
        print(f"{self.name} is walking...")

    # String Metodu (__str__) - Nesneyi yazdırdığında nasıl görüneceğini belirler
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer: {self.name}"

# Nesne Tabanlı Programlama - Class'tan Örnekleme
human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk()

human2 = Human("Halit")
human2.talk("Selam")
human2.walk()

