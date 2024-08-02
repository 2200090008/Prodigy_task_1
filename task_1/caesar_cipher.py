def caesar_cipher(text, shift, mode='encrypt'):
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    # Normalize the shift for large values
    shift = shift % len(alphabet)

    # Adjust the shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Preserve the case
            is_upper = char.isupper()
            base = 'A' if is_upper else 'a'
            index = (ord(char) - ord(base) + shift) % 26
            result += chr(ord(base) + index)
        else:
            # Keep non-alphabetic characters unchanged
            result += char

    return result

# Get user input
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))
operation = input("Do you want to 'encrypt' or 'decrypt'? ").lower()

# Map abbreviations to full operation names
if operation == 'e':
    operation = 'encrypt'
elif operation == 'd':
    operation = 'decrypt'

# Perform the operation
if operation == 'encrypt':
    encrypted_message = caesar_cipher(message, shift_value, mode='encrypt')
    print("Encrypted Message:", encrypted_message)
elif operation == 'decrypt':
    decrypted_message = caesar_cipher(message, shift_value, mode='decrypt')
    print("Decrypted Message:", decrypted_message)
else:
    print("Invalid operation. Please choose 'encrypt' or 'decrypt'.")
