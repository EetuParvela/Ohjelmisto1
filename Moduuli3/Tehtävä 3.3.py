gender = input("Oletko mies vai nainen?: ").lower()

while True:
    try:
        hemoglobin = float(input("Anna hemoglobiiniarvosi (g/l): "))
        break
    except ValueError:
        print("Virhe. Anna hemoglobiiniarvo numeroina.")

if gender == "nainen":
    if hemoglobin < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117 <= hemoglobin <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
elif gender == "mies":
    if hemoglobin < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134 <= hemoglobin <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
else:
    print("Virhe. Kirjoita mies tai nainen.")