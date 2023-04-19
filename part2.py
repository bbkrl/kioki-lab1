def multiplicative_encrypt_decrypt(text: str, key: int, mode: str) -> str:
    """
    This function takes a string, a key and a mode as arguments and returns the encrypted or decrypted text
    using the Multiplicative Cipher algorithm.

    Parameters:
    text (str): The text to be encrypted or decrypted
    key (int): The key to be used for encryption or decryption
    mode (str): The mode to be used. Either 'encrypt' or 'decrypt'

    Returns:
    str: The encrypted or decrypted text
    """
    try:
        # Check if the key is valid
        if key < 1 or key > 25:
            raise ValueError("Key must be between 1 and 25")

        # Check if the mode is valid
        if mode not in ['encrypt', 'decrypt']:
            raise ValueError("Mode must be either 'encrypt' or 'decrypt'")

        # Define the alphabet and its length
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_len = len(alphabet)

        # Define the output string
        output = ''

        # Loop through each character in the text
        for char in text:
            # Check if the character is a letter
            if char.isalpha():
                # Convert the character to lowercase
                char = char.lower()

                # Get the index of the character in the alphabet
                char_index = alphabet.index(char)

                # Encrypt or decrypt the character based on the mode
                if mode == 'encrypt':
                    new_index = (char_index * key) % alphabet_len
                else:
                    # Find the modular inverse of the key
                    for i in range(alphabet_len):
                        if (key * i) % alphabet_len == 1:
                            inverse_key = i
                            break
                    new_index = (char_index * inverse_key) % alphabet_len

                # Get the new character from the alphabet
                new_char = alphabet[new_index]

                # Add the new character to the output string
                output += new_char
            else:
                # Add non-letter characters to the output string
                output += char

        # Return the output string
        return output
    except ValueError as e:
        # Log the error
        print(f"Error: {e}")
        return ''

if __name__ == '__main__':
    print(multiplicative_encrypt_decrypt('hello world', 7, 'encrypt'))
    print(multiplicative_encrypt_decrypt('xczzu yupzv', 7, 'decrypt'))