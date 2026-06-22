from password_checker import check_password_strength
from password_generator import generate_password
from password_cracker import dictionary_attack

def main():
    print("==== Password Security Project ====")
    print("1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Simulate Password Cracking")
    
    choice = input("Enter choice: ")

    if choice == "1":
        password = input("Enter password: ")
        strength, feedback = check_password_strength(password)
        print("Strength:", strength)

        if feedback:
            print("Suggestions:")
            for f in feedback:
                print("-", f)

    elif choice == "2":
        length = int(input("Enter password length: "))
        print("Generated Password:", generate_password(length))

    elif choice == "3":
        password = input("Enter password to test: ")

        with open("common_passwords.txt", "r") as file:
            wordlist = file.readlines()

        found, attempts = dictionary_attack(password, wordlist)

        if found:
            print(f"Password cracked in {attempts} attempts!")
        else:
            print(f"Password NOT cracked after {attempts} attempts.")

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()