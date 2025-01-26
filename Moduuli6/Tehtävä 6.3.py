# Funktio muuttaa USA:n gallonat litroiksi
# käyttäen virallista 1l=3,785gallona muunnoskerrointa.
def gallons_to_litres(gallon):
        litres = gallon * 3.785
        print(f"{gallon} gallonaa on {litres:.2f} litraa.")
        return litres

while True:
    try:
        user_input = float(input("Anna nesteen määrä gallonoina: "))
        if user_input < 0:
            print("Annoit negatiivisen luvun, lopetetaan ohjelma.")
            break
        gallons_to_litres(user_input)
    except ValueError:
        print("Virhe! Syötä vain numeroita.")


