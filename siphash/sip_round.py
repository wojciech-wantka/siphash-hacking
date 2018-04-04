from operator import xor

from siphash.parameters import Parameters

from siphash.utils import rol


def half_sip_round_core(state, a, b, c, d):
    state[a] = (state[a] + state[1]) % Parameters.modulus
    state[b] = (state[b] + state[3]) % Parameters.modulus
    state[1] = rol(state[1], c, 64)
    state[3] = rol(state[3], d, 64)
    state[1] = xor(state[1], state[a])
    state[3] = xor(state[3], state[b])
    state[a] = rol(state[a], 32, 64)


def half_sip_round(state, mode):
    (a, b, c, d) = (0, 2, 13, 16) if mode == 0 else (2, 0, 17, 21)

    half_sip_round_core(state, a, b, c, d)


def sip_round(state):
    half_sip_round(state, 0)
    half_sip_round(state, 1)
