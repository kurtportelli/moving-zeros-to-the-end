def move_zeros(array):
    new_array = []
    n_zeros = 0
    for element in array:
        if repr(element) == '0' or repr(element) == '0.0':
            n_zeros += 1
        else:
            new_array.append(element)
    new_array.extend([0] * n_zeros)
    return new_array
