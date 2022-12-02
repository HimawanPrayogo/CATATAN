kalimat=input("masukan kalimat:")
angka=int(input("masukan angka:"))

def left(kalimat,angka):
    a=kalimat[0:angka]
    return a

hasil=left(kalimat,angka)
print(hasil)
