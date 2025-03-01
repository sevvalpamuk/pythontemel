def asal_mi(sayi):
    if sayi < 2:
        print(f"{sayi}  asal sayı değildir.")
    
    for i in range(2, int(sayi ** 0.5) + 1):  
        
        if sayi % i == 0:
             print( f"{sayi}  asal sayı değildir.")
    
    return f"{sayi} asal sayıdır."


def hesap_makinesi(sayi1, sayi2, islem):
    if islem == '+':
        print( f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
    elif islem == '-':
        print( f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
    elif islem == '*':
         print( f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
    elif islem == '/':
        if sayi2 == 0:
           print("Bölme işlemi için ikinci sayı 0 olamaz")
        print( f"{sayi1} / {sayi2} = {sayi1 / sayi2}")
    else:
        print("Geçersiz işlem türü")


print(asal_mi(7))  
print(asal_mi(10)) 

print(hesap_makinesi(5, 3, '+'))  
print(hesap_makinesi(10, 2, '/'))
print(hesap_makinesi(4, 0, '/'))  
print(hesap_makinesi(6, 2, '%')) 