from differential_cryptoanalysis.inverse_sip_round import inverse_sip_round
from siphash.sip_round import sip_round


def main():
    test_data = [
        [0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000],
        [0x3648365828047382, 0x2758265902648194, 0x5746184027471957, 0x5639104759174057]
    ]

    for test_case in test_data:
        input_value = test_case.copy()

        sip_round(input_value)
        inverse_sip_round(input_value)

        assert input_value == test_case
