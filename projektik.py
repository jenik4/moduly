import random

moznosti = ["kámen", "nůžky", "papír"]

while True:
    uzivatel = input("Vyber kámen, nůžky nebo papír, pokud chceš skončit napiš konec: ")

    if uzivatel == 'konec':
        break

    pocitac = random.choice(moznosti)
    print(f"Počítač vybral: {pocitac}")

    if uzivatel in moznosti:
        if uzivatel == pocitac:
            print("je to remíza")
        elif (uzivatel == "kámen" and pocitac == "nůžky") or \
             (uzivatel == "nůžky" and pocitac == "papír") or \
             (uzivatel == "papír" and pocitac == "kámen"):
            print("Vyhrál jsi gg")
        else:
            print("Prohrál jsi gg")
    else:
        print("Asi jsi něco napsal špatně, zkus to znovu.")