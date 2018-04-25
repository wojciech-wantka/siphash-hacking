from siphash.mode import Mode

from differential_cryptoanalysis.inverse_sip_round import inverse_sip_round
from siphash.sip_round import sip_round_generic


def main():
    test_data = [
        [0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000],
        [0xffffffffffffffff, 0xffffffffffffffff, 0xffffffffffffffff, 0xffffffffffffffff],
        [0x3648365828047382, 0x2758265902648194, 0x5746184027471957, 0x5639104759174057],
        [0x1b4d7a9e3725ce84, 0x1637506846264957, 0x564926194624ef96, 0xabef47bb88360486],
        [0x39f076a00fff9bab, 0x3a052c4ac43a32ad, 0x782930ebd33b266a, 0x5772b657935e9480],
        [0x3617315be83345f1, 0xf33b0e5358958084, 0x0ebb78d491b69056, 0x9f27637b732ee528]
    ]

    for test_case in test_data:
        input_value = test_case.copy()

        sip_round_generic(input_value, Mode.LINEARIZED)
        inverse_sip_round(input_value)

        assert input_value == test_case
