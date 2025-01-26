names = set()

while True:
        user_input = input("Kirjoita nimi tai paina ENTER lopettaaksesi ohjelman: ").strip()

        if not user_input:
            break

        if user_input in names:
            print("Aiemmin syötetty nimi.")
        else:
            print("Uusi nimi.")
            names.add(user_input)

print("Syöttämäsi nimet olivat: ")
for name in names:
    print(name)