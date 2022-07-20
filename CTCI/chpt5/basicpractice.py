# see if n is a power of two
# NOTE & is the bitwise operator for bit manipulation and

# time complexity is O(lgn)
def power_of_2(x):
    if x == 0 | x == 1:
        return False
    return (x and not (x & (x - 1)))


# print(0, power_of_2(0))
# print(1, power_of_2(1))
# print(2, power_of_2(2))
# print(3, power_of_2(3))
# print(4, power_of_2(4))
# print(5, power_of_2(5))
# print(8, power_of_2(8))

# count the number of ones in the bit form of the number
# ? How do i get the bit form of the number x & x-1?

# time will run in O(k) where k is the number of ones in the binary form of n
def count_ones(n):
    count = 0
    while (n):
        # all bits from the right most one are being flipped and reasigned. This will increment until n = 0
        # every & operation with x and (x-1) will result in one less 1 in its bit
        n = n & (n-1)
        # print(n)
        count += 1

    return count


# print(0, count_ones(0))
# print(1, count_ones(1))
# print(1, count_ones(2))
# print(2, count_ones(3))
# print(3, count_ones(7))


# 1 should be i as 2^i
def check_ith(n):
    print(n & (n << 1))
    if n & (n << 1):
        return True
    else:
        return False


# print(check_ith(1))
# print(check_ith(2))
# print(check_ith(3))
# print(check_ith(4))

# gets the bit of i and returns Treu if 1 False if 0
def get_bit(num, i):
    return ((num & (1 << i)) != 0)


# logical statement walk through
# * A = 9 = 1001, i = 1 = 0001:
# * ((1001 & (1 << 0001)) != 0) = (( 1001 & 0010 )) != 0
# * ((( 1001 & 0010 )) != 0) = (0000 != 0) = False
# print(True, get_bit(9, 0))
# print(False, get_bit(9, 1))
# print(False, get_bit(9, 2))
# print(True, get_bit(9, 3))
# print(True, get_bit(3, 1))

# ! you cannot set bits backwards 9 cannot go to 8, 7 cannot go to 3


def set_bit(num, i):
    return num | (1 << i)

# * process
# * num = 9 = 1001:
# * 1001 | (0001) << 1
# * 1001 | 0010
# * 1011 = 11

# print(11, set_bit(9, 1))
# print(7, set_bit(7, 0))

# ? clear bits

# clearing bits


def clear_bit(num, i):
    return num & (not (1 << i))


print(clear_bit(9, 3))


def clear_bits_through_i(num, i):
    mask = (1 << i) - 1
    return num & mask


def clear_bits_to_0(num, i):
    mask = (-1 << (i + 1))
    return num & mask


def update_bit(num, i, bit_is_1):
    value = 1 if bit_is_1 else 0
    mask = not (1 << i)
    return (num & mask) | (value << i)

# * update_bit(num, i, 0 | 1)
