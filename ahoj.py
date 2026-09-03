text = "Ahoj jak se mas"

slova = text.split()

cetnosti = {}

for word in slova:
    delka = len(word)

    if delka in cetnosti:
        cetnosti[delka] += 1
    else:
        cetnosti[delka] = 1

print(cetnosti),