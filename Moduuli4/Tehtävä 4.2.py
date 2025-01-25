luku = float(input("Anna luku tuumina: "))

while luku > 0:
    sentit = luku * 2.54
    print(f"{luku} on senttimetreinä {sentit}")
    luku = float(input("Anna luku tuumina: "))
else:
    print("Näkemiin.")