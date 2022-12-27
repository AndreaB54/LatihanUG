print("="*10, "PROGRAM PENGHITUNG PYTHAGORAS", "="*10)
bil1 = int(input("Masukkan bilangan bulat pertama: "))
bil2 = int(input("Masukkan bilangan bulat kedua: "))
bil3 = int(input("Masukkan bilangan bulat ketiga: "))

#rumus
if ((bil1**2)+(bil2**2)) == (bil3**2):
    print("Merupakan Pythagoras.")
elif ((bil3**2)-(bil1**2)) == (bil2**2):
    print("Merupakan Pythagoras.")
elif ((bil3**2)-(bil2**2)) == (bil1**2):
    print("Merupakan Pythagoras.")
else :
    print("Bukan Merupakan Pythagoras.")