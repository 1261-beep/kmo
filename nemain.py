users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

uživatel = input("Uživatelské jméno: ")
heslo = input("Heslo: ")

if uživatel not in users or users[uživatel] != heslo:
    print("Špatné uživatelské jméno nebo heslo, terminace programu...")
    exit()


balanc = 100


while True:
    if balanc <= 0:
        print("prohrál si")
        exit()

    print("Toto jsou vaše kredity:", balanc)
    print("Každý roll stojí 10 kreditů")

    souhlas = input("chcete rollovat? A/N: ")

    if souhlas not in ("N", "A"):
        print("Špatný vstup")
        continue

    elif souhlas == "A":
        balanc -= 15
        print("rolluji...")
        import random

        ovoce = ["🍎","🍌","🍇","🍓","🍒","🍍"]

        a = random.choice(ovoce)
        b = random.choice(ovoce)
        c = random.choice(ovoce)

        vyhry = (a, b, c)
        print(a, b, c)

        if a == b == c == "🍍":
            print("MEGA ULTRA JACKPOT!!!")
            balanc += 10000

        elif a == b == c == "🍒":
            print("ULTRA JACKPOT!!!")
            balanc += 1000

        elif a == b == c:
            print("JACKPOT!!!")
            balanc += 100

        elif a == b or a == c or b == c:
            print("výhra!")
            balanc += 30

        else:
            print("nic")

        if "🍒" in vyhry:
            balanc += 10
            print("BONUS 🍒 +10")

        if "🍍" in vyhry:
            balanc += 20
            print("BONUS 🍍 +20")

    elif souhlas == "N":
        print("Končíš s:", balanc, "kreditama")
        break
