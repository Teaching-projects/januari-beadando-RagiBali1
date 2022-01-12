print("Magyarul vagy angolul szeretnel beszelgetni?")
nyelv = input("Add meg a nyelvet: ")
if nyelv == "magyar":
    print("Hello!")
    nev = input("Add meg  neved kerlek: ")
    print("Hello!", nev, "Minecraft vagy Warzone?")
    valasztas1 = input("Válassz!: ")
    if valasztas1 == "Minecraft":
        print("Nincs mirol beszelnunk.")
    if valasztas1 == "Warzone":
        print("Gyere igyunk mg valamit! De elotte mondd meg az eletkorodat legyszives.")
        kor = int(input("Add meg eletkorod: "))
        if kor >= 18:
            print("Akkor menjun sorozni!")
        else:
            print("Akkor ebbol almale lesz!")
if nyelv == "angol":
    print("Hi!")
    nev = input("What's your name?: ")
    print("Hi!", nev, "Mincraft or Warzone?")
    valasztas1 = input("Choose!: ")
    if valasztas1 == "Miinecraft":
        print("Don't talk with me!")
    if valasztas1 == "Warzone":
        print("Come, drink something! But, how old are you?")
        kor = int(input("Your age: "))
        if kor >= 18:
            print("Let's drink a beer!")
        else:
            print("You can have only Apple juice! :)")