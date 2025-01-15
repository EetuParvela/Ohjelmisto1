import random

three_digit_code = "".join(str(random.randint(0, 9)) for _ in range(3))
four_digit_code = "".join(str(random.randint(1,6)) for _ in range(4))

print(f"Kolmenumeroinen koodi on {three_digit_code} ja nelinumeroinen koodi on {four_digit_code}.")