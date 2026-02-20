
while True:
        try:
                age = int(input("# Ievadi vecumu: "))

                if age < 0:
                        print("# Vecums nevar būt negatīvs!")
                        continue
                if age > 130:
                        print("# Vecums pārāk liels!")
                        continue
                break
        except ValueError:
                print("# Vecumam jābūt skaitlim!")

while True:
        license_input = input("# Vai ir autovadītāja apliecība? (j/n): ").lower()

        if license_input == "j":
                if age < 18:
                        print(f"# Jums nevar būt autovadītāja apliecība {age} gadu vecumā! Lūdzu atbildiet pareizi.")
                        continue
                license = True
                break
        elif license_input == "n":
                license = False
                break
        else:
                print("# Atbildei ir jābūt jā vai nē!")

while True:
        student_input = input("# Vai ir students? (j/n): ").lower()

        if student_input == "j":
                if age < 16:
                        print(f"# {age} gadu vecumā Jūs esat pārāk jauns lai skaitītos par studentu! Lūdzu atbildiet pareizi.")
                        continue
                student = True
                break
        elif student_input == "n":
                student = False
                break
        else:
                print("# Atbildei ir jābūt jā vai nē!")

while True:
        veteran_input = input("# Vai ir veterāns? (j/n): ").lower()

        if veteran_input == "j":
                if age < 55:
                        print(f"# Pēc valsts likuma, Jūs nevarat būt veterāns, ja Jūums nav sākot no 55 gadu vecuma! Lūdzu atbildiet pareizi.")
                        continue
                veteran = True
                break
        elif veteran_input == "n":
                veteran = False
                break
        else:
                print("# Atbildei ir jābūt jā vai nē!")

can_vote = age >= 18
can_rent = age >= 21 and license
senior_discount = age >= 65 or veteran
student_discount = 16 <= age <= 26 and student

def yes_no(value):
        return "Jā ✓" if value else "Nē ✗"

vote_text = yes_no(can_vote)

if can_rent:
        rent_text = "Jā ✓"
else:
        if age < 18:
                rent_text = "Nē ✗"
        elif not license:
                rent_text = "Nē ✗ (nav apliecības)"
        else:
                rent_text = "Nē ✗ (par jaunu lai īrētu)"

senior_text = yes_no(senior_discount)
student_text = yes_no(student_discount)

print("# ---")
print(f"# Balsošana: {vote_text}")
print(f"# Auto īre: {rent_text}")
print(f"# Senioru atlaide: {senior_text}")
print(f"# Studentu atlaide: {student_text}")