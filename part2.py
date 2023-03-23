# def encode(string, key=7, n=26):
#     if key > 26:
#         key = key % 26
#
#     encoded_text = ''
#     for char in string:
#         if ord('a') <= ord(char) <= ord('z'):
#             if ord(char) + key > ord('z'):
#                 encoded_text = encoded_text + chr((ord(char)*key) % n)
#             else:
#                 encoded_text = encoded_text + chr(ord(char) * key)
#         elif ord('A') <= ord(char) <= ord('Z'):
#
#     return encoded_text
#
#
# if __name__ == '__main__':
#     print(encode(string='kiryl'))

def encrypt(source_text, key):
    n = 256  # Assuming ASCII codes
    if not are_coprime(key, n):
        raise ValueError("Key and alphabet size must be coprime")
    encrypted_text = ""
    for char in source_text:
        # Multiply the character code by the key, modulo n
        encrypted_char = chr((ord(char) * key) % n)
        encrypted_text += encrypted_char
    return encrypted_text


def are_coprime(a, b):
    """Return True if a and b are coprime (have no common factors other than 1)"""
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(encrypt('kiryl', 7))
