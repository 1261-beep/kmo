#Ahoj, jmenuji se Matyáš Smetana a tohle je moje Bulls and Cows hra






import random

print("------------------------------------------------")
print("Ahojky")
print("------------------------------------------------")
print("Vygeneroval jsem pro tebe náhodné 4místné číslo")
print("Zkus ho uhádnout!")
print("Je to hra Býci a Krávy")
print("------------------------------------------------")

tajne_cislo = ''.join(random.sample('123456789', 4))


attempts = 0

while True:
    guess = input("Tak tipuj: ")

    if not guess.isdigit():
        print("Pouze čísla!")
        continue

    if len(guess) != 4:
        print("4 číslice!")
        continue

    if len(set(guess)) != 4:
        print("Číslice se nesmí opakovat!")
        continue

    attempts += 1

    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == tajne_cislo[i]:
            bulls += 1

    for i in range(4):
        if guess[i] != tajne_cislo[i] and guess[i] in tajne_cislo:
            cows += 1

    print("Býci:", bulls)
    print("Krávy:", cows)
    print("------------------------------------------------")

    if bulls == 4:
        break

print("🎉 Máš to!")

if attempts == 1:
    print("Wow, v jednom pokusu!")
else:
    print(f"Zvládl jsi to v {attempts} pokusech!")