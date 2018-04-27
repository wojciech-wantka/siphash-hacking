from siphash.siphash import siphash_linearized


def return_generator_matrix(key, compression_rounds, finalization_rounds, message_length):
    generator_matrix = message_length * [None]

    number = 0x01

    for i in range(message_length):
        message = list(map(lambda byte: int(byte), number.to_bytes(message_length, byteorder='little')))
        _, generator_matrix[i] = siphash_linearized(key, message, compression_rounds, finalization_rounds)

        number <<= 1

    return generator_matrix
