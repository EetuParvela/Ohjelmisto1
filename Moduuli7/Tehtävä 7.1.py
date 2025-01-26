seasons = ("talvi", "kevät", "kesä", "syksy")

while True:
    try:
        user_input = int(input("Anna kuukauden numero (1-12): "))
        if 1 <= user_input <= 12:
            break
        else:
            print("Virhe! Kirjoita luku 1-12 väliltä.")
    except ValueError:
        print("Virhe! Syötä vain kokonaislukuja.")

season_number = (user_input % 12) // 3
season = seasons[season_number]

print(f"{user_input}. kuukauden vuodenaika on {season}.")