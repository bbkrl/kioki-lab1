def rail_fence_cipher(clear_text, key):
    print(f'original text: {clear_text}')

    result = ''
    matrix = [["" for _ in range(len(clear_text))] for _ in range(key)]

    increment = 1
    row = 0
    col = 0

    for c in clear_text:
        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1

        matrix[row][col] = c

        row += increment
        col += 1

    for element in matrix:
        result += ''.join(element)

    return result


if __name__ == '__main__':
    text = 'Hello World!'
    dec = rail_fence_cipher(text, 3)
    print(dec)
