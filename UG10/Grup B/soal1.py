print("~"*15, " /('v')\ ", "~"*15)
print("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print("~"*15, " \('v')/ ", "~"*15)
print("")

print("Pilihlah salah satu bangun ruang yang ingin dihitung volumenya:\n1. Limas\n2. Bola\n3. Prisma\n4. Kerucut")
print("")

pilih = int(input("Masukkan pilihan Anda: "))

#rumus
if pilih == 1:
    sisi = int(input("Masukkan panjang sisi alas limas: "))
    tinggi = int(input("Masukkan tinggi limas: "))
    limas = ((1/3)*(sisi**2)*tinggi)
    print ("Volume limas tersebut adalah", limas)

elif pilih == 2:
    jari = int(input("Masukkan panjang jari-jari bola: "))
    bola = ((4/3)*(3.14*(jari**3)))
    print ("Volume bola tersebut adalah", bola)

elif pilih == 3:
    print("Pilihlah salah satu dari pilihan di bawah:\n1. Prisma Segitiga\n2. Prisma Segiempat\n3. Prisma Segilima")
    pilihan = int(input("Tentukan pilihan Anda: "))
    if pilihan == 1:
        alas = int(input("Masukkan panjang sisi alas prisma: "))
        talas = int(input("Masukkan tinggi alas prisma: "))
        tprisma = int(input("Masukkan tinggi prisma segitiga: "))
        ptiga = (((alas*talas)/2)*tprisma)
        print ("Volume prisma segitiga tersebut adalah", ptiga)
    elif pilihan == 2:
        alas = int(input("Masukkan panjang sisi alas prisma: "))
        talas = int(input("Masukkan tinggi alas prisma: "))
        tprisma = int(input("Masukkan tinggi prisma segiempat: "))
        pempat = (alas*talas*tprisma)
        print ("Volume prisma segiempat tersebut adalah", pempat)
    elif pilihan == 3 :
        alas = int(input("Masukkan panjang sisi alas prisma: "))
        talas = int(input("Masukkan tinggi alas prisma: "))
        tprisma = int(input("Masukkan tinggi prisma segilima: "))
        plima = (((5*alas*talas)/2)*tprisma)
        print ("Volume prisma segilima tersebut adalah", plima)
    else:
        print("Prisma yang Anda cari belum tersedia di Kalkulator ini")

elif pilih == 4:
    jari = int(input("Masukkan jari-jari kerucut: "))
    tinggi = int(input("Masukkan tinggi kerucut: "))
    kerucut = ((1/3)*3.14*(jari**2)*tinggi)
    print ("Volume kerucut tersebut adalah", kerucut)