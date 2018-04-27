from operator import xor

from siphash.mode import Mode
from siphash.parameters import Parameters

from siphash.utils import rol


def half_sip_round_generic(state, a, b, c, d, mode):
    if mode == Mode.STANDARD:
        state[a] = (state[a] + state[1]) % Parameters.modulus
        state[b] = (state[b] + state[3]) % Parameters.modulus
    else:
        state[a] = xor(state[a], state[1])
        state[b] = xor(state[b], state[3])

    state[1] = rol(state[1], c, Parameters.state_word_length)
    state[3] = rol(state[3], d, Parameters.state_word_length)
    state[1] = xor(state[1], state[a])
    state[3] = xor(state[3], state[b])
    state[a] = rol(state[a], 32, Parameters.state_word_length)


def sip_round_generic(state, mode):
    (a, b, c, d) = Parameters.parameters(0)
    half_sip_round_generic(state, a, b, c, d, mode)

    (a, b, c, d) = Parameters.parameters(1)
    half_sip_round_generic(state, a, b, c, d, mode)


def sip_round(state):
    sip_round_generic(state, Mode.STANDARD)


def sip_round_linearized(state):
    sip_round_generic(state, Mode.LINEARIZED)
