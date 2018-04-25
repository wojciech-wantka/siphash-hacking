from operator import xor

from siphash.parameters import Parameters

from siphash.utils import ror


def inverse_half_sip_round(state, a, b, c, d):
    state[a] = ror(state[a], 32, Parameters.state_word_length)
    state[3] = xor(state[3], state[b])
    state[1] = xor(state[1], state[a])
    state[3] = ror(state[3], d, Parameters.state_word_length)
    state[1] = ror(state[1], c, Parameters.state_word_length)
    state[b] = xor(state[b], state[3])
    state[a] = xor(state[a], state[1])


def inverse_sip_round(state):
    (a, b, c, d) = Parameters.parameters(1)
    inverse_half_sip_round(state, a, b, c, d)

    (a, b, c, d) = Parameters.parameters(0)
    inverse_half_sip_round(state, a, b, c, d)
