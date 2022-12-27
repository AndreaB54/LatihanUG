panjang=int(input("Masukkan panjang : "))
lebar=int(input("Masukkan lebar : "))
jari=int(input("Masukkan jari-jari : "))

persegi = panjang*lebar
lingkaran = (1/2)*(22/7)*(jari**2)
print("Area tersebut membutuhkan",(round((persegi+lingkaran)/15)),"kaleng cat")