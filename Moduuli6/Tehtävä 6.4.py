# Funktio ottaa listan kokonaislukuja ja laskee niiden summan.
def list_numbers_sum(numbers):
    result = sum(numbers)
    return result

numbers_list = []

while True:
    try:
        user_input = input("Syötä numero tai paina ENTER lopettaaksesi ohjelman: ")
        if user_input == "":
            print("Lopetit ohjelman.")
            print(f"Antamasi lukujen summa on {list_numbers_sum(numbers_list)}.")
            break
        numbers_list.append(int(user_input))
    except ValueError:
        print("Virhe! Syötä vain kokonaislukuja.")

