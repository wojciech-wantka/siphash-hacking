import tests.inverse_sip_round_test
import tests.siphash_test


def main():
    tests.siphash_test.main()
    tests.inverse_sip_round_test.main()


if __name__ == '__main__':
    main()
