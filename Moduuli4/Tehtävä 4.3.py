numbers_list = []
biggest_number = 0
smallest_number = 0
number = input("Anna luku: ")

while number != "":
    numbers_list.append(number)
    biggest_number = max(numbers_list)
    smallest_number = min(numbers_list)
    number = input("Anna luku: ")
else:
    print(f"Lopetit ohjelman. Suurin numero oli {biggest_number} ja pienin numero oli {smallest_number}.")