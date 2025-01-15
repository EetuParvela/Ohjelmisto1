kuha_length = float(input("Mikä on kuhan pituus?: "))
kuha_allowed_length = 37

if kuha_length >= kuha_allowed_length:
    print(f"Kuha on sallitun pituinen.")
else:
    print(f"Kuha on {kuha_allowed_length-kuha_length}cm liian lyhyt.")