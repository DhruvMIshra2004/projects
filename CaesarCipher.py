import string
import random

# Function to encode text using Caesar Cipher with added randomness
def encode_random_caesar(text, key):
    special_chars = ['@', '#', '$', '%', '&', '*', '!', '?', '^', '~', '_']  # Now defined inside function
    result = ''
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase

    for i in text:
        if i in uppercase:
            index = (uppercase.index(i) + key) % 26
            ch = uppercase[index]
            ch = ch.lower() if random.choice([True, False]) else ch
            result += ch + random.choice(special_chars)
        elif i in lowercase:
            index = (lowercase.index(i) + key) % 26
            ch = lowercase[index]
            ch = ch.upper() if random.choice([True, False]) else ch
            result += ch + random.choice(special_chars)
        elif i == ' ':
            result += random.choice(['_', '~', '-'])  # Replace space
        else:
            result += i + random.choice(special_chars)
    return result

# Function to decode the encrypted Caesar Cipher while removing special characters
def decode_random_caesar(text, key):
    cleaned = ''
    for i in text:
        if i in string.ascii_letters:
            cleaned += i
        elif i in ['_', '~', '-']:
            cleaned += ' '
        else:
            continue
    return decode_caesar_cipher(cleaned, key)

# Original Caesar decode function
def decode_caesar_cipher(text, key):
    result = ''
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase

    for i in text:
        if i in uppercase:
            index = (uppercase.index(i) - key) % 26
            result += uppercase[index]
        elif i in lowercase:
            index = (lowercase.index(i) - key) % 26
            result += lowercase[index]
        else:
            result += i
    return result

# User interface
def main_menu():
    while True:
        print("\n----------- Upgraded Caesar Cipher Menu -----------")
        print("1. Encode Plain Text")
        print("2. Decode Cipher Text")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter plain text to encode: ")
            key = int(input("Enter the key: "))
            cipher_text = encode_random_caesar(text, key)
            print("Encrypted Cipher Text:\n", cipher_text)
        elif choice == '2':
            text = input("Enter the encrypted cipher text: ")
            key = int(input("Enter the key used for encryption: "))
            plain_text = decode_random_caesar(text, key)
            print("Decrypted Plain Text:\n", plain_text)
        elif choice == '3':
            print("Thank you for using the Caesar Cipher program!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

# Run the program
main_menu()
