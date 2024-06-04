import random
import string

def gen_pass(len, use_alphabets, use_num, use_symbols):
    characters = ""
    if use_alphabets:
        characters += string.ascii_letters
    if use_num:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "No character is selected!"

    password = ""
    for _ in range(len):
        password += random.choice(characters)

    return password

def main():
    print("Welcome to My Password Generator!")

    len = int(input("Enter the length of the password: "))
    use_alphabets = input("Include alphabets (Y/N): ").upper() == 'Y'
    use_num = input("Include numbers (Y/N): ").upper() == 'Y'
    use_symbols = input("Include symbols (Y/N): ").upper() == 'Y'

    password = gen_pass(len, use_alphabets, use_num, use_symbols)

    print("Generated Password Is:", password)

if __name__ == "__main__":
    main()