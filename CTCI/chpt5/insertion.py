# CTCI 5.1

# insertion
# insert a bit number in m from i to j
# the bits are 32 bit

def insertion(n, m, i, j):
    len_n = len(str(n)) - 2
    mask_start = "0" * (len_n - j)
    mask_end = "0" * i
    masked_m = int(mask_start + str(m) + mask_end)
    masked_n = (((mask_start) + (len(str(m)) * "1") + mask_end))
    print(float(masked_n))

    # update masked area
    # print(update_bits(n, i, j))


def update_bits(n, i, j):
    for k in range(i, j+1):

        mask_left = len(str(n)) * "0"
        mask = ~(1 << k)
        print(mask)
        # print(x)
        n = mask & n
        print(n)
    return n


print(insertion(100000111100, 10011, 2, 6))
