# def caeser_encoder(k:int):
#     """k - шаг шифрования"""
#     alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#     # k = int(input('Шаг шифрования'))
#
#     lang = input('Выберите язык RU/EU: ').lower()
#     message = input('Строка для шифрования').upper()
#
#     result = ''
#
#     if lang == 'ru':
#         for i in message:
#             place = alphabet_RU.find(i)
#             new_place = place + k
#             if i in alphabet_RU:
#                 result += alphabet_RU[new_place]
#             else:
#                 result += i
#     else:
#         for i in message:
#             place = alphabet_EU.find(i)
#             new_place = place + k
#             if i in alphabet_EU:
#                 result += alphabet_EU[new_place]
#             else:
#                 result += i
#
# def caeser_decoder():
#

def cipher(s, n):
    if s > 26:
        s = s % 26
    caesar = ''
    for i in n:
        if ord('a') <= ord(i) <= ord('z'):
            if ord(i) + s > ord('z'):
                caesar = caesar + chr((ord(i) + s) - 26)
            else:
                caesar = caesar + chr(ord(i) + s)
        elif ord('A') <= ord(i) <= ord('Z'):
            if ord(i) + s > ord('Z'):
                caesar = caesar + chr((ord(i) + s) - 26)
            else:
                caesar = caesar + chr(ord(i) + s)
        else:
            caesar = caesar + i
    return caesar


def dec(s, n):
    if s > 26:
        s = s % 26
    caesar = ''
    for i in n:
        if ord('a') <= ord(i) <= ord('z'):
            if ord(i) - s < ord('a'):
                caesar = caesar + chr((ord(i) - s) + 26)
            else:
                caesar = caesar + chr(ord(i) - s)
        elif ord('A') <= ord(i) <= ord('Z'):
            if ord(i) - s < ord('A'):
                caesar = caesar + chr((ord(i) - s) + 26)
            else:
                caesar = caesar + chr(ord(i) - s)
        else:
            caesar = caesar + i
    return caesar


if __name__ == '__main__':
    s = int(input("Введите ключ - "))
    n = input("Введите текст - ")

    encrypted = cipher(s, n)
    decrypted = dec(s, encrypted)

    print(f'encrypted - {encrypted}\ndecrypted - {decrypted}')
