# Bit Manipulation

## Atributes

#### Aside all operators work with the same syntax in python

### not (~)
#### Swaps all bits (1s turn into 0s and 0s turn into 1s in all locations)
  `
  A = 0101 = 5: ~A = 1010 = 10
  B = 0011 = 3: ~B = 1100 = 14
  `

### and (&)
#### Two bits of equal length are compared anywhere a 1 and a 0 match up it is a 0
  `
  A = 4 = 100, B = 3 = 011: A & B = 000
  C = 8 = 1000, D = 7 = 0111: C & D = 0000
  `

### or (|)
#### Two bits of equal length are compared. Anyhwere patterns of two 0s than 0 otherwise 1
  `
  A = 4 = 100, B = 3 = 011: A | B = 111 = 7
  C = 8 = 1000, D = 1 = 0001: C | D = 1001 = 9
  E = 9 = 1001, F = 11 = 1011: E | F = 1011 = 11
  `
### xor (^)
#### Two bits of equal length are compared. Anywhere patterns of two 0s and 1s reside than 0 otherwise 1. If the two bits in comparison are not equal than 1.
  `
  A = 3 = 011, B = 5 = 101: A^B = 011 ^ 101 = 110 = 6
  C = 8 = 1000, D = 2 = 0010: C^D = 1000 ^ 0010 = 1010 = 10
  `

### left shift (<<)
#### Move the bits left by k. 1 << k = 2^k
  `
  A = 4 = 0100: A << 3 = 100000 = 2^5 = 32
  B = 9 = 1001: B << 2 = 100100 = 2^5 + 2^2 = 36
  `

### right shift (>>)
#### Move the bits right by k.
  `
  A = 4 = 0100: A >> 3 = 0000 = 0
  B = 9 = 1001: B >> 2 = 0010 = 2^1 = 2
  C = 11 = 1011: C >> 1 = 0101 = 2^2 + 2^0 = 5
  `