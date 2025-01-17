number = input("Kirjoita luku: ")
number_list = []

while number != "":
    number_list.append(number)
    number = input("Kirjoita toinen luku: ")

number_list.sort(reverse=True)

print(number_list[:5])