import random

# Funktio ottaa listan kokonaislukuja
# ja palauttaa uuden listan vain parillisia lukuja alkuperäisestä listasta.
def get_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

while True:
    try:
        user_input = int(input("Syötä listan pituus: "))
        break
    except ValueError:
        print("Virhe! Syötä vain kokonaislukuja.")

all_numbers = [random.randint(1, 1000) for _ in range(user_input + 1)]

even_numbers = get_even_numbers(all_numbers)
print(f"Lista kaikista numeroista: {all_numbers}")
print(f"Lista vain parillisista numeroista {even_numbers}")