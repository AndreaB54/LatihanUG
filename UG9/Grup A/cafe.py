print("="*20 +"CAFE"+"="*20)
print("="*10 +"MASUKKAN JUMLAH PESANAN"+"="*10)
cappucino = int(input("CAPPUCINO\tDISKON 50%\tRp 25.000\t:  "))
latte = int(input("VANILLA LATTE\tDISKON 65%\tRp 22.000\t:  "))
americano = int(input("AMERICANO\tDISKON35%\tRp 30.000\t:  "))
coffe = int(input("BREWED COFFEE\tDISKON40%\tRp. 20.000\t :  "))
print("")

#mesin
cappucino = cappucino * (25000 - (25000*0.5))
latte = latte * (22000 - (22000*0.65))
americano = americano * (30000 - (30000*0.35))
coffe = coffe * (20000 - (20000*0.4))

#output
print("="*18 + "TOTAL" + "="*18)
print("TOTAL CAPPUCINO\t: Rp", cappucino)
print("TOTAL VANILLA LATTE\t: Rp", latte)
print("TOTAL AMERICANO\t: Rp", americano)
print("TOTAL BREWED COFFEE\t: ", coffe)
print("Jumlah total biaya yang harus dibayar adalah Rp", float(cappucino+latte+americano+coffe))