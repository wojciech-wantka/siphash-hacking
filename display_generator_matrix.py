import enum

from differential_cryptoanalysis.return_generator_matrix import return_generator_matrix


class GeneratorMatrixDisplayFormat(enum.Enum):
    TXT = 1
    SAGE = 2


def bitfield(number, number_of_bits):
    bit_array = [int(digit) for digit in bin(number)[2:]]
    return [0] * (number_of_bits - len(bit_array)) + bit_array


def display_generator_matrix(generator_matrix, generator_matrix_display_format):
    if generator_matrix_display_format == GeneratorMatrixDisplayFormat.TXT:
        for hash_value in generator_matrix:
            print('{:064b}'.format(hash_value))
    else:
        print('generator_matrix=matrix(GF(2), [')

        for i in range(len(generator_matrix) - 1):
            print('{},'.format(bitfield(generator_matrix[i], 64)))

        print(bitfield(generator_matrix[len(generator_matrix) - 1], 64))

        print('])')


def main():
    compression_rounds = 2
    finalization_rounds = 4
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e]
    message_length = 512

    generator_matrix_display_format = GeneratorMatrixDisplayFormat.SAGE

    generator_matrix = return_generator_matrix(key, compression_rounds, finalization_rounds, message_length)

    display_generator_matrix(generator_matrix, generator_matrix_display_format)


if __name__ == '__main__':
    main()
