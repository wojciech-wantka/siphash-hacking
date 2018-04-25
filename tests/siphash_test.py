from siphash.siphash import siphash


def zero_byte_sequences_with_different_length_should_have_different_hash():
    key = [0xaa, 0x8d, 0xfb, 0xf4, 0x80, 0x88, 0x5c, 0x9f, 0x5c, 0xd7, 0x06, 0x06, 0x95, 0x06, 0x5c, 0x91]
    message1 = [0x00, 0x00, 0x00, 0x00, 0x00]
    message2 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    _, output1 = siphash(key, message1, 2, 4)
    _, output2 = siphash(key, message2, 2, 4)

    assert output1 != output2


def implementation_tests():
    zero_key = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    reference_key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

    from_paper = [
        reference_key,
        [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e],
        2,
        4,
        0xa129ca6149be45e5
    ]

    with_zero_key = [
        [
            zero_key,
            [0x00] * 8,
            2,
            4,
            0xe849e8bb6ffe2567
        ],
        [
            zero_key,
            [],
            2,
            4,
            0x1e924b9d737700d7
        ],
        [
            zero_key,
            [0x00] * 1535,
            2,
            4,
            0xe74d1c0ab64b2afa
        ],
        [
            zero_key,
            [ord(c) for c in '12345678123'],
            2,
            4,
            0xf95d77ccdb0649f
        ],
        [
            zero_key,
            [ord(c) for c in 'Hello world'],
            2,
            4,
            0xc9e8a3021f3822d9
        ]
    ]

    test_data = [from_paper]
    test_data += with_zero_key

    for test_case in test_data:
        _, output = siphash(test_case[0], test_case[1], test_case[2], test_case[3])

        assert output == test_case[4]


def main():
    zero_byte_sequences_with_different_length_should_have_different_hash()
    implementation_tests()
