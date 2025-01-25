import random

dice_sum = 0

while True:
    try:
        user_input = int(input("Kuinka monta noppaa heitetään?: "))
        break
    except ValueError:
        print("Anna vastaus numerona.")

for _ in range(user_input):
    dice_sum += random.randint(1, 6)

print(f"Heitettyjen noppien summa oli {dice_sum}.")
