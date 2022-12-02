print("++++++++++ PROGRAM KONVERSI SUHU ++++++++++")

suhu=int(input("Masukan Skala Celcius:"))

def suhu_reamur():
    a=suhu*4/5
    return a

def suhu_farenheit():
    b=suhu*9/5+32
    return b

def suhu_kelvin():
    c=suhu+273
    return c

a1=suhu_reamur()
b1=suhu_farenheit()
c1=suhu_kelvin()

print("Hasil Konversi Suhu",suhu,"C","adalah",a1,"Reamur")
print("Hasil Konversi Suhu",suhu,"C","adalah",b1,"Farenheit")
print("Hasil Konversi Suhu",suhu,"C","adalah",c1,"Kelvin")
