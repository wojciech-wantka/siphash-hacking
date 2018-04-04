from math import ceil
from operator import xor

from siphash.sip_round import sip_round
from siphash.utils import reduce


def init_internal_state(key):
    temp_key = [reduce(key[0: 8]), reduce(key[8: 16])]

    state = [None] * 4

    state[0] = xor(temp_key[0], 0x736f6d6570736575)
    state[1] = xor(temp_key[1], 0x646f72616e646f6d)
    state[2] = xor(temp_key[0], 0x6c7967656e657261)
    state[3] = xor(temp_key[1], 0x7465646279746573)

    return state


def parse(message):
    parsed_message_length = ceil((len(message) + 1) / 8)

    parsed_message = [None] * parsed_message_length

    for i in range(parsed_message_length - 1):
        parsed_message[i] = reduce(message[i * 8: (i + 1) * 8])

    strip_length = len(message) % 8
    end = len(message) % 256

    parsed_message[parsed_message_length - 1] = reduce(message[len(message) - strip_length: len(message)] + [0] * (8 - strip_length - 1) + [end])

    return parsed_message


def compress(state, parsed_message, compression_rounds, history):
    for parsed_message_word in parsed_message:
        state[3] = xor(state[3], parsed_message_word)

        for _ in range(compression_rounds):
            sip_round(state)
            history.append(state.copy())

        state[0] = xor(state[0], parsed_message_word)


def finalize(state, finalization_rounds, history):
    state[2] = xor(state[2], 0xff)

    for _ in range(finalization_rounds):
        sip_round(state)
        history.append(state.copy())


def siphash(key, message, compression_rounds, finalization_rounds):
    history = []
    state = init_internal_state(key)
    history.append(state.copy())
    parsed_message = parse(message)
    compress(state, parsed_message, compression_rounds, history)
    finalize(state, finalization_rounds, history)
    output = xor(xor(state[0], state[1]), xor(state[2], state[3]))

    return history, output
