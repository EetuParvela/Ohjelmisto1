import random

# Funktio ottaa nopan suurimman mahdollisen silmäluvun
# ja heittää nopan palauttaen saadun silmäluvun.
def throw_dice(max_value):
    dice_number = random.randint(1, max_value)
    print(f"Nopan silmäluku oli {dice_number}")
    return dice_number

while True:
    try:
        user_input = int(input("Mikä on nopan maksimi silmäluku?: "))
        break
    except ValueError:
        print("Virhe! Syötä vain numeroita.")

while True:
    result = throw_dice(user_input)
    if result == user_input:
        print("Nopan maksimi silmäluku saatiin.")
        break