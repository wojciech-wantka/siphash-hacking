1. Find MWCILC (minimum weight isn't a must - some low weight can be sufficient)

2. If low weight codeword is found, then we can approximate the probability that linear elements behaves just like non-linear elements (if codeword contains many zeroes "0", then this probability is small, because there are many multiplications by 1/2).

3. Find library for MWCW:
    1. start with NTL (because it has optimized algorithm, but it may be hard to use).
    2. if NTL is too hard to use, then check if implementation from article:

    ```
    Leif Both, Alexander May, "Decoding Linear Codes with High Error Rate and Its Impact for LPN Security"
    ```

    can be used. The implementation is located at

    ```
    https://github.com/LeifBoth/Decoding-LPN.
    ```
