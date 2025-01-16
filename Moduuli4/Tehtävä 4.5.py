username = "python"
password = "rules"
login_tries = 0

login_username = input("Kirjoita käyttäjä tunnus: ")
login_password = input("Kirjoita salasana: ")

while login_username != username and login_password != password and login_tries < 5:
    print("Käyttäjätunnus tai salasana on väärin. Kokeile uudelleen.")
    login_tries += 1
    login_username = input("Kirjoita käyttäjä tunnus: ")
    login_password = input("Kirjoita salasana: ")
    if login_tries == 5:
        print("Pääsy evätty.")
        exit()
else:
    print("Tervetuloa sisään.")