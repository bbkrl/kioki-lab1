import pandas as pd
import numpy as np
from textwrap import wrap

grid_size = 6
grid_template = (
    '..X..X',
    '.X....',
    '...X..',
    '.X..X.',
    'X....X',
    '..X...')

init_string = 'itdf12gdce34aton56qrdi78qwer90yui123321iuy09rewq87idrq65no'
encoded_string = '31ie5twduo0q38af7re1iy26g4itddr2cqn9w-3-r2-1-i----8i--euo-yq0q-7n95-r6d-'


def split_string_by_9_symbols(string, n=9):
    return [string[i:i+n] for i in range(0, len(string), n)]


def split_and_fill_string_by_36_symbols(init_string):
    list_of_srtings_by_36_symbols = wrap(init_string, 36)
    if len(list_of_srtings_by_36_symbols[-1]) != 36:
        list_of_srtings_by_36_symbols[-1] = list_of_srtings_by_36_symbols[-1].ljust(36, '-')
    return list_of_srtings_by_36_symbols


def prepare_grid(grid_template):
    data = (grid_template,)
    df = pd.DataFrame(list(data), index=['grid', 'code']).T
    grid_arr = df.grid.str.extractall(r'(.)').unstack().eq('X').values
    return grid_arr


def encode_string(grid_points, grid_size, lists_of_substrings):
    res_list = []
    for substring in range(len(lists_of_substrings)):
        grid = np.full((grid_size, grid_size), 'X')
        for rotation in range(4):
            if rotation != 0:
                grid = np.rot90(grid, -1)
            for i in range(len(grid_points)):
                x_i = grid_points[i][0]
                y_i = grid_points[i][1]
                grid[x_i, y_i] = lists_of_substrings[substring][rotation][i]
        grid = np.rot90(grid, -1)

        print(grid)

        for i in range(6):
            for j in range(6):
                res_list.append(grid[i][j])

    return res_list


def decode_string(grid_points, grid_template, lists_of_substrings):
    res_list = []
    for substring in range(len(lists_of_substrings)):
        df = pd.DataFrame(list((grid_template, lists_of_substrings[substring])), index=['grid', 'code']).T
        data_arr = df.code.str.extractall(r'(.)').unstack().values
        print(data_arr)

        for rotation in range(4):
            if rotation != 0:
                data_arr = np.rot90(data_arr, -1)
            for i in range(len(grid_points)):
                x_i = grid_points[i][0]
                y_i = grid_points[i][1]
                res_list.append(data_arr[x_i, y_i])
        data_arr = np.rot90(data_arr, -1)

    return "".join(res_list).replace('-', '')


def encoder_decoder3(grid_size, grid_template, init_str, mode='encode'):
    grid_arr = prepare_grid(grid_template)

    grid_points = []
    for i in range(len(grid_arr)):
        for j in range(len(grid_arr[i])):
            if grid_arr[i][j] == True:
                grid_points.append((i, j))

    if mode == 'encode':
        list_of_strings_by_36_symbols = split_and_fill_string_by_36_symbols(init_str)
        lists_of_substrings = [split_string_by_9_symbols(substring) for substring in list_of_strings_by_36_symbols]
        res_list = encode_string(grid_points, grid_size, lists_of_substrings)
        return ''.join(res_list)

    if mode == 'decode':
        list_of_strings_by_36_symbols = [init_str[i:i + 36] for i in range(0, len(init_str), 36)]
        lists_of_substrings = [[substring[i:i + 6] for i in range(0, len(substring), 6)] for substring in
                               list_of_strings_by_36_symbols]
        res_list = decode_string(grid_points, grid_template, lists_of_substrings)
        return res_list


if __name__ == '__main__':
    encoder_decoder3(grid_size, grid_template, encoded_string, mode='decode')