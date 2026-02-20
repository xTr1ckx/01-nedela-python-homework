import random

def valid_guess(guess):
    return 1 <= guess <= 100

while True:
    guessing_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 10
    previous_guesses = set()

    print("# Uzspēlējam minēšanas spēli! Jums ir 10 mēģinājumi uzminēt skaitli no 1 līdz 100!")

    while True:

        guess_input = input("# Tavs minējums: ")
    
        try:
            guess = int(guess_input)
        except ValueError:
            print("# Minējumam ir jābūt veselam skaitlim no 1 līdz 100!")
            continue

        if guess in previous_guesses:
            print("# Jūs jau iepriekš minējāt šo skaitli.")
            continue
        else:
            previous_guesses.add(guess)

        if not valid_guess(guess):
            print("# Minējumam ir jābūt veselam skaitlim no 1 līdz 100!")
            continue
        
        attempts += 1

        if guess == guessing_number:
            print(f"# Pareizi! Atbilde bija {guessing_number}.")
            print(f"# Atbilde sasniegta {attempts} mēģinājumos.")
            break
        elif guess < guessing_number:
            print("# Par mazu.")
            print(f"# Šis bija jūsu {attempts}. mēģinājums.")
        else:
            print("# Par lielu.")
            print(f"# Šis bija jūsu {attempts}. mēģinājums.")

        if attempts >= max_attempts:
            print(f"# Mēģinājumu limits sasniegts! Minējamais skaitlis bija {guessing_number}.")
            break

    again = input("# Vai vēlaties spēlēt vēlreiz? (j/n)").lower()
    if again != "j":
        break

