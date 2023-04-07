import string
from textwrap import wrap
from copy import deepcopy

def number_key(key_phrase):
    key_list = list(key_phrase)
    sorted_list_key = sorted(key_phrase)
    sorted_key = ''.join(sorted_list_key)
    deepcopy_sorted_list_key = deepcopy(sorted_list_key)
    keyword_indexes = []
    for i in range(len(key_list)):
        symbol_index = deepcopy_sorted_list_key.index(key_list[i])
        keyword_indexes.append(symbol_index)
        deepcopy_sorted_list_key[symbol_index] = "Q"

    # letters = tuple(string.ascii_lowercase)
    #
    # key_phrase = key_phrase.lower()
    # key_number = list(key_phrase)
    #
    # counter = 0
    #
    # for letter_index, letter_value in enumerate(letters):
    #     for key_index, key_value in enumerate(key_phrase):
    #         if letter_value == key_value:
    #             key_number[key_index] = counter
    #             counter += 1

    return keyword_indexes


def key_phrase_encryption(text, key):
    key = number_key(key)
    len_key = len(key)

    text_array = wrap(text.replace(' ', '!'), len_key)
    if len(text_array) != len_key:
        text_array[-1] = text_array[-1].ljust(len_key, '@')

    chiphered_text = []
    for i in range(len(text_array)):
        deepcopy_key = deepcopy(key)
        for j in range(len(deepcopy_key)):
            chiphered_text.append(text_array[i][deepcopy_key.index(min(deepcopy_key))])
            deepcopy_key[deepcopy_key.index(min(deepcopy_key))] = 100
    result = ''.join(chiphered_text)
    return result


def key_phrase_decryption(text, key):
    key = number_key(key)
    len_key = len(key)

    text_array = wrap(text, len_key)
    if len(text_array) != len_key:
        text_array[-1] = text_array[-1].ljust(len_key, '@')

    dechiphered_text = []

    for i in range(len(text_array)):
        for j in range(len(key)):
            dechiphered_text.append(text_array[i][key[j]])

    result = ''.join(dechiphered_text)

    return result.replace('!', ' ').replace('@', ' ')


if __name__ == '__main__':

    a = key_phrase_encryption('This is a lecture on encryption algorithms', 'cryptography')
    # print(a, sep='\n')
    print(a, key_phrase_decryption(a, 'cryptography'))