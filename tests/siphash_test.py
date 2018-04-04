from siphash.siphash import siphash


def main():
    test_data = [
        [
            [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F],
            [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E],
            2,
            4,
            0xa129ca6149be45e5
        ],
        [
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            2,
            4,
            0xe849e8bb6ffe2567
        ],
        [
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [],
            2,
            4,
            0x1e924b9d737700d7
        ],
        [
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [0] * 1535,
            2,
            4,
            0xe74d1c0ab64b2afa
        ],
        [
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [ord(c) for c in '12345678123'],
            2,
            4,
            0xf95d77ccdb0649f
        ],
        [
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [ord(c) for c in 'Hello world'],
            2,
            4,
            0xc9e8a3021f3822d9
        ]
    ]

    for test_case in test_data:
        _, output = siphash(test_case[0], test_case[1], test_case[2], test_case[3])

        assert output == test_case[4]
