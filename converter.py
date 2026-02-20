KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020

print("Izvēlies konversiju:")
print("1) km <-> mi")
print("2) kg <-> lb")
print("3) l <-> gal")
print("4) usd <-> eur")

conversion = input("> ")

if conversion == "1":
        print("Virziens:")
        print("1) km -> mi")
        print("2) mi -> km")
        direction = input("> ")

        while True:
                try:
                        value = float(input("Ievadi vērtību: "))
                        break
                except ValueError:
                        print("Ievadītā vērtība nav skaitlis!")

        if direction == "1":
                result = value * KM_TO_MI
                print(f"{value:.2f} km = {result:.2f} mi")
        elif direction == "2":
                result = value / KM_TO_MI
                print(f"{value:.2f} mi = {result:.2f} km")

elif conversion == "2":
        print("Virziens:")
        print("1) kg -> lb")
        print("2) lb -> kg")
        direction = input("> ")

        while True:
                try:
                        value = float(input("Ievadi vērtību: "))
                        break
                except ValueError:
                        print("Ievadītā vērtība nav skaitlis!")

        if direction == "1":
                result = value * KG_TO_LB
                print(f"{value:.2f} kg = {result:.2f} lb")
        elif direction == "2":
                result = value / KG_TO_LB
                print(f"{value:.2f} lb = {result:.2f} kg")

elif conversion == "3":
        print("Virziens:")
        print("1) l -> gal")
        print("2) gal -> l")
        direction = input("> ")

        while True:
                try:
                        value = float(input("Ievadi vērtību: "))
                        break
                except ValueError:
                        print("Ievadītā vērtība nav skaitlis!")

        if direction == "1":
                result = value * L_TO_GAL
                print(f"{value:.2f} l = {result:.2f} gal")
        elif direction == "2":
                result = value / L_TO_GAL
                print(f"{value:.2f} gal = {result:.2f} l")

elif conversion == "4":
        print("Virziens:")
        print("1) usd -> eur")
        print("2) eur -> usd")
        direction = input("> ")

        while True:
                try:
                        value = float(input("Ievadi vērtību: "))
                        break
                except ValueError:
                        print("Ievadītā vērtība nav skaitlis!")

        if direction == "1":
                result = value * USD_TO_EUR
                print(f"{value:.2f} usd = {result:.2f} eur")
        elif direction == "2":
                result = value / USD_TO_EUR
                print(f"{value:.2f} eur = {result:.2f} usd")

else:
        print("Nepareiza izvēle! Izvēlieties skaitli no 1 līdz 4.")

