linearization = replace additions with xors

question: when addition = xor?

answer: when carry doesn't occur (carry occur <=> both bits are set to "1")

Remarks:

* linearized model is "3/4-equivalent" of original model
* for 32-bit word: Probability(addition = xor) = (3/4) ^ 32
* this probability can be improved when words have small amount of "1" (for there is smaller chance that both "1" would meet in the same position)

***

Definitions:

* H := differential path (history of hash computation)
* x_0 := 10000...
* x_1 := 01000...
* x_2 := 00100...

Approach:

1. find such message in linearized model, that has smallest amount of "1" in H
2. move back from linearized model to original model (this is why the small amount of "1" is desired - we are reducing probability of error)

Since in linearized model we have

    L(x XOR y) = L(x) XOR L(y),

then H is linear function. So we can compute

    H(x_0), H(x_1), H(x_2), etc.

Then we have

    H(x_i XOR x_j) = H(x_i) XOR H(x_j).

Remark: Differential path is linear combination of snapshots.

***

Thus the question can be reduced to known problem: "finding minimum weight codeword in a linear code".

Usage: error correcting codes (systems based on error correcting codes are resilient to quantum attacks)

Computer algebra systems that can find minimum weight codeword in a linear code:

* Magma: http://magma.maths.usyd.edu.au/magma/
* SageMath: http://www.sagemath.org/
* NTL (Number Theory Library): http://www.shoup.net/ntl/

***

Observation: Sip rounds are invertible, so we can begin from middle and then compute some fragment forward, and some fragment backward.

***

General remarks:

* Siphash is an example of more general class of functions -- Feistel ciphers.
