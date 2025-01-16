import random

i=0
n=0

N = input("Kuinka monta satunnaista pistettä laitetaan: ")

while i < int(N):
    x_coordinate = random.random()
    y_coordinate = random.random()
    if (x_coordinate ** 2 + y_coordinate ** 2) < 1:
        n += 1
    else:
        pass
    i += 1

pi = 4*n/int(N)

print(f"Piin likiarvo {N} pisteellä on {pi}.")