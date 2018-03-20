from operator import xor

from siphash.siphash import siphash


def return_differences(key, compression_rounds, finalization_rounds, message_1, message_2):
    history_1, _ = siphash(key, message_1, compression_rounds, finalization_rounds)
    history_2, _ = siphash(key, message_2, compression_rounds, finalization_rounds)

    differences = [None] * len(history_1)

    for i in range(len(differences)):
        differences[i] = list(map(xor, history_1[i], history_2[i]))

    return differences
