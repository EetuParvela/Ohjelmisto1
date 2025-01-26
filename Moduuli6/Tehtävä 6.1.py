import random

# Funktio heittää nopan ja printtaa ja palauttaa saadun silmäluvun.
def throw_dice():
    number = random.randint(1, 6)
    print(f"Nopan silmäluku oli {number}")
    return number

while True:
    result = throw_dice()
    if result == 6:
        print("Silmäluku oli kuusi, lopetetaan ohjelma.")
        break