def luas_segitiga(alas, tinggi):
    luas=0.5*alas*tinggi
    return luas

alas=int(input("masukan alas:"))
tinggi=int(input("masukan tinggi:"))
a=luas_segitiga(alas, tinggi)
print(a)
