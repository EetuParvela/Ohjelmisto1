gender = input("Oletko mies vai nainen?: ").strip().upper()

if gender == "MIES":
    normal_min = 134
    normal_max = 195
elif gender == "NAINEN":
    normal_min = 117
    normal_max = 175
else:
    print("Virhe: Kirjoita mies tai nainen.")
    exit()

try:
    hemoglobin = float(input("Anna hemoglobiiniarvosi (g/l): "))
except ValueError:
    print("Virheellinen hemoglobiini arvo. Anna arvo numeroina (g/l).")
    exit()

if hemoglobin < normal_min:
    condition = "alhainen"
elif normal_min <= hemoglobin <= normal_max:
    condition = "normaali"
else:
    condition = "korkea"

print(f"Sinulla on {condition} hemoglobiiniarvo.")