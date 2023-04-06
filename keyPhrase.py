import string


def number_key(key_phrase):
    letters = tuple(string.ascii_lowercase)

    key_phrase = key_phrase.lower()
    key_number = [i for i in key_phrase]

    counter = 1

    for letter_index, letter_value in enumerate(letters):
        for key_index, key_value in enumerate(key_phrase):
            if letter_value == key_value:
                key_number[key_index] = counter
                counter += 1

    return key_number


def key_phrase_encryption(text, key):
    key = number_key(key)
    text_array = [text[i:i+(len(key))] for i in range(0, len(text), (len(text) // (len(key))))]

    chiphered_text = []

    for index, value in enumerate(text_array):
        for i in range(len(value)):
            for index_key, item in enumerate(key):
                if i == item:
                    chiphered_text.append(value[index_key])


if __name__ == '__main__':
    print(number_key('KiRyl'))