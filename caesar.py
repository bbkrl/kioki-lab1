import string


def caesar_cipher(text, shift):
    """
    This function takes a string and a shift value and returns the Caesar cipher of the string.

    Parameters:
    text (str): The string to be encrypted
    shift (int): The shift value for the cipher

    Returns:
    str: The encrypted string
    """
    try:
        # Check if shift value is within range
        if shift < 0 or shift > 25:
            raise ValueError("Shift value must be between 0 and 25")

        # Create a translation table for the cipher
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted_alphabet)

        # Return the encrypted string
        return text.translate(table)
    except ValueError as e:
        # Log the error
        print(f"Error: {e}")
        return ""


def caesar_decrypt(ciphertext, shift):
    """
    This function takes a ciphertext and a shift value and returns the decrypted plaintext using the Caesar cipher.

    Parameters:
    ciphertext (str): The encrypted message
    shift (int): The number of positions to shift the letters

    Returns:
    str: The decrypted plaintext
    """
    try:
        # Check if shift is within the range of 1 to 25
        if shift < 1 or shift > 25:
            raise ValueError("Shift value must be between 1 and 25")

        # Decrypt the ciphertext
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                # Shift the letter by the specified amount
                shifted_char = chr((ord(char.lower()) - 97 - shift) % 26 + 97)
                plaintext += shifted_char.upper() if char.isupper() else shifted_char
            else:
                plaintext += char

        return plaintext
    except ValueError as e:
        # Log the error
        print(f"Error: {e}")
        return ""


if __name__ == '__main__':
    pass
