import math

# Funktio ottaa pizzan halkaisijan, hinnan ja muuttaa ne muotoon eur/m^2.
def pizza_square_meter_price(diameter, price):
    area_m = (math.pi * (diameter/2) ** 2) / 10000
    price_per_m2 = price / area_m
    return price_per_m2

while True:
    try:
        diameter1 = float(input("Syötä ensimmäisen pizzan halkaisija senttimetreinä: "))
        price1 = float(input("Syötä ensimmäisen pizzan hinta: "))
        diameter2 = float(input("Syötä toisen pizzan halkaisija senttimetreinä: "))
        price2 = float(input("Syötä toisen pizzan hinta: "))
        break
    except ValueError:
        print("Virhe! Syötä vain numeroita. ")

m2_price1 = pizza_square_meter_price(diameter1, price1)
m2_price2 = pizza_square_meter_price(diameter2, price2)

if m2_price1 < m2_price2:
    print(f"Ensimmäisen pizzan neliöhinta on {m2_price1:.2f} euroa "
          f"ja toisen pizzan neliöhinta on {m2_price2:.2f} euroa, joten "
          f"ensimmäinen pizza tarjoaa paremman vastineen rahalle.")
elif m2_price2 < m2_price1:
    print(f"Ensimmäisen pizzan neliöhinta on {m2_price1:.2f} euroa "
          f"ja toisen pizzan neliöhinta on {m2_price2:.2f} euroa, joten "
          f"toinen pizza tarjoaa paremman vastineen rahalle.")
else:
    print("Pizzojen neliöhinta on sama.")