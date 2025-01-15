leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
luoti_weight = 0.0133
naula_factor = 32
leiviskä_factor = 20

weight = ((luodit * luoti_weight) + (naulat * (naula_factor * luoti_weight)) +
          (leiviskät * (leiviskä_factor * (naula_factor * luoti_weight))))
kilos, grams = divmod(weight, 1)
print(f"Massa nykymittojen mukaan: {int(kilos)} kilogrammaa ja {(grams * 1000):.2f} grammaa.")