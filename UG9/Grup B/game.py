name = str(input("STATE YOUR NAME: "))
print("="*110)
print("")

print("<"*10, "Adventure of", name, ">"*10)
print("")

print("Welcome to the Adventure of", name, "!")
print("")

print("Are you a Male / Female? [M/F]")
gender = str(input(">> "))
print("")
print("")
print("")

print("One day, A young adventurer named", name)
print("spawned in a peacefull Village of Orion")
print(name, "walked out of village and see a slime jumping around.")
print("")

print("picked up a... (Sword/Bow)")
alat = str(input(">> "))
print("and attack the slime.")

#alat
if "Sword" in alat:
    print("the slime get sliced and died. adventurer gain a level.")

elif "Bow" in alat :
    print("the slime get shot and died. adventurer gain a level.")

else:
    print("You Lose...")
print("")

print(name, "The Adventurer, then run towards a chest that glows from the inside\nPICK ONE!\n[OPEN/WALK]")
pilih = str(input(">> "))
print("")

#pilih
if "Open" in pilih :
    print("The Adventurer Finds a Gold and brings it Home to the Village.")
    print("")

elif "Walk" in pilih :
    print("The Adventurer has just missed a chance and bring nothing on the way back home.")
    print("")

print("as the adventure walks, he started to feel more and more tired.\nTake a [Break] / Keep [Walk]ing")
lanjut = str(input(">> "))
print("")

#lanjut
if "Break" in lanjut :
    print(name, "meet a tiger at the forest\n" + name, "tried to beat them but because", name, "feel very tired", name, ", can't beat them and lose")
    print("GAME OVER")
    exit ()

elif "Walk" in lanjut :
    print(name, "Arrived at the village and see RTX 3090 Ti on sale\nWith the price of 1 gold")
    belanja = str(input("[BUY] / [PASS]>> "))
    if "Buy" in belanja :
        print("Congratulation! you got your dream stuff!\nNow you can play Minecraft with Raytracing FOREVER!\n\nAnd live Happily ever After!~~")
    elif "Pass" in belanja :
        print("Congratulation! you have accomplish your game!\n\nAnd live Happily ever After!~~")
