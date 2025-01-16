gender = input("Oletko mies vai nainen?: ").upper()

if gender == "MIES":
    normal_min = 134
    normal_max = 195
elif gender == "NAINEN":
    normal_min = 117
    normal_max = 175
else:
    print("Virhe: Kirjoita mies tai nainen.")
    exit()

hemoglobin = float(input("Anna hemoglobiiniarvosi (g/l): "))

if hemoglobin < normal_min:
    condition = "alhainen"
elif normal_min <= hemoglobin <= normal_max:
    condition = "normaali"
else:
    condition = "korkea"

print(f"Sinulla on {condition} hemoglobiiniarvo.")