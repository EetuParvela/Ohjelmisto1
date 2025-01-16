import random

dice_amount = input("Kuinka monta noppaa heitetään?: ")
dice_sum = 0

for i in range(int(dice_amount)):
    dice_sum += random.randint(1, 6)
    i += 1

print(f"Heitettyjen noppien summa on {dice_sum}")
