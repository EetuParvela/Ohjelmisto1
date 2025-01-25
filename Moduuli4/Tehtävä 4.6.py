import random

points_inside_circle=0

while True:
    try:
        random_points = int(input("Kuinka monta satunnaista pistettä kokeillaan: "))
        break
    except ValueError:
        print("Anna vastaus numeroina.")

i = 0
while i <= random_points:
    x_coordinate = random.random()
    y_coordinate = random.random()
    if (x_coordinate ** 2 + y_coordinate ** 2) < 1:
        points_inside_circle += 1
    i += 1

pi = 4*points_inside_circle/int(random_points)

print(f"Piin likiarvo {random_points} pisteellä on {pi}.")