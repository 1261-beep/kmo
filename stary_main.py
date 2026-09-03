users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uživatel = input("Uživatelské jméno: ")
heslo = input("Heslo: ")


if uživatel in users and users[uživatel] == heslo:
    print("Vítejte",uživatel,"!")
    print("Máme",len(TEXTS),"texty na analyzování.")
    vyber = int(input(f"Napište číslo 1 až {len(TEXTS)} pro výběr textu k analýze: "))
    print(" ")

else:
    print("Špatné uživatelské jméno nebo heslo, terminace programu...")
    exit()

def name(vyber):
    print(TEXTS[vyber - 1])
    print("     ")
    print("Zde jsou parametry textu:")
    print("---------------------------------------------------")
    parametr_slova = TEXTS[vyber - 1].split()
    print("V textu je",len(parametr_slova),"slov")

    slovicka = 0
    for word in parametr_slova:
        if word[0].isupper():
            slovicka += 1
    print("V textu je",slovicka,"slov začínajících velkým písmenem")
    
    slovka = 0
    for wor in parametr_slova:
        if wor.isupper():
            slovka += 1
    print("V textu je",slovka,"slov psaných velkým písmem")

    slov = 0
    for work in parametr_slova:
        if work.islower():
            slov += 1
    print("V textu je",slov,"slov psaných malým písmem")

    cisla = 0
    for ceslo in parametr_slova:
        if ceslo.isnumeric():
            cisla += 1
    print("V textu je",cisla,"cisel")

    ciesla = 0
    for ceselo in parametr_slova:
        if ceselo.isnumeric():
            ciesla += int(ceselo)
    print("Součet čísel v textu je",ciesla)
    print(" ")
    print("Zde je délka slov a jak často se objevují")
    print("---------------------------------------------------")

    data = {}
    
    for word in parametr_slova:
        if len(word) in data:
            data[len(word)] += 1
        else:
            data[len(word)] = 1

    sorted_data = dict(sorted(data.items()))
    
    print("LEN|OCCURRENCES          |NR.")
    print("---------------------------------------------------")

    for key, value in sorted_data.items():
        print(f"{key:<3}| {'*' * value:<20}| {value}")
        
name(vyber)
