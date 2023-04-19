def railfence_cipher(message, key):
    """
    This function encrypts a message using the Rail Fence Cipher technique.

    Parameters:
    message (str): The message to be encrypted
    key (int): The number of rails to use for the cipher

    Returns:
    str: The encrypted message
    """
    try:
        # Check if the key is a positive integer
        if not isinstance(key, int) or key <= 0:
            raise ValueError("Key must be a positive integer")

        # Remove any spaces and convert message to uppercase
        message = message.replace(" ", "").upper()

        # Create a list of empty strings for each rail
        rails = [""] * key

        # Fill the rails with the message
        rail_index = 0
        direction = 1
        for char in message:
            rails[rail_index] += char
            rail_index += direction
            if rail_index == 0 or rail_index == key - 1:
                direction *= -1

        # Combine the rails into the encrypted message
        encrypted_message = "".join(rails)

        return encrypted_message
    except ValueError as e:
        # Log the error
        print(f"Error: {e}")
        return ""


def decrypt_railfence(cipher, key):
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix to
    # distinguish filled spaces
    # from blank ones
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    # to find the direction
    dir_down = None
    row, col = 0, 0

    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        rail[row][col] = '*'
        col += 1

        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1

    # now we can construct the
    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
                    (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):

        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return ("".join(result))


if __name__ == '__main__':
    text = 'Hello World!'
    dec = rail_fence_cipher(text, 3)
    print(dec)
