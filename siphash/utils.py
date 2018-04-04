from collections import deque


def reduce(array):
    reduction = 0

    for i in range(len(array)):
        reduction += array[i] * 256 ** i

    return reduction


def rotate(number, bits, length):
    array = list(bin(number)[2:])
    array.reverse()
    array += ['0'] * (length - len(array))
    d = deque(array)
    d.rotate(bits)
    array = list(d)
    array.reverse()

    return int(''.join(array), 2)


def rol(number, bits, length):
    return rotate(number, bits, length)


def ror(number, bits, length):
    return rotate(number, -bits, length)
