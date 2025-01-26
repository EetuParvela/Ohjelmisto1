# Funktio kysyy käyttäjältä ICAO-koodin ja lentokentän nimen, tarkistaa onko koodi jo käytössä
# ja lisää uuden lentokentän sanakirjaan, jos koodilla ei ole aiemmin tallennettua arvoa.
def add_airport():
    icao_code = input("Kirjoita lentokentän ICAO-koodi: ").strip().upper()

    if icao_code in airports:
        print(f"ICAO-koodilla {icao_code} on jo olemassa lentokenttä {airports[icao_code]}.")
    else:
        airport_name = input("Kirjoita lentokentän nimi: ").strip()
        airports[icao_code] = airport_name
        print(f"{airport_name} lentokenttä on lisätty koodilla {icao_code}.")

    return airports

# Funktio kysyy käyttäjältä ICAO-koodin ja tarkistaa löytyykö sille arvoa
# lentokenttien sanakirjasta.
def check_airport():
    icao_code = input("Anna haettavan lentokentän ICAO-koodi:").strip().upper()

    if icao_code in airports:
        print(f"Hakemasi lentokentän nimi on {airports[icao_code]}.")
    else:
        print("Syöttämälläsi ICAO-koodilla ei löytynyt tallennettua arvoa.")

airports = {}

while True:
    user_input = input("Kirjoita A lisätäksesi uuden lentokentän, kirjoita B hakeaksesi lentokentän "
                       "tai paina ENTER lopettaaksesi ohjelman. ").strip().lower()

    if user_input == "a":
        add_airport()
    elif user_input == "b":
        check_airport()
    elif not user_input:
        print("Lopetit ohjelman.")
        break
    else:
        print("Virhe! Syötä vain A, B tai paina ENTER lopettaaksesi ohjelman.")