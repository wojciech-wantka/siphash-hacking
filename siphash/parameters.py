class Parameters:
    state_word_length = 64
    modulus = 1 << state_word_length

    @staticmethod
    def parameters(phase):
        return (0, 2, 13, 16) if phase == 0 else (2, 0, 17, 21)
