while True:
    try:
        number = int(input("Anna kokonaisluku: "))
        break
    except ValueError:
        print("Kirjoita kokonaisluku.")

if number <= 1:
    print(f"{number} ei ole alkuluku.")
else:
    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            print(f"{number} ei ole alkuluku.")
            break
    else:
        print(f"{number} on alkuluku.")



