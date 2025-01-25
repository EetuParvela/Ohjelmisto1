import random

random_number = random.randint(1, 10)
quessed_number = int(input("Arvaa luku 1 ja 10 väliltä: "))

while quessed_number != random_number:
    if quessed_number < random_number:
        print("Liian pieni arvaus.")
        quessed_number = int(input("Arvaa uudestaan: "))
    elif quessed_number > random_number:
        print("Liian suuri arvaus.")
        quessed_number = int(input("Arvaa uudestaan: "))
else:
    print("Arvasit oikein.")

