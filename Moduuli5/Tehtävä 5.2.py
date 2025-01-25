number_list = []

while True:
    user_input = input("Syötä luku tai paina ENTER lopettaaksesi ohjelman: ").strip()

    if user_input == "":
        break

    try:
        number = int(user_input)
        number_list.append(number)
    except ValueError:
        print("Virhe. Syötä luku numerona.")

number_list.sort(reverse=True)

print("Viisi suurinta lukua olivat: ", end=" ")
for number in number_list[:5]:
    print(number, end=" ")