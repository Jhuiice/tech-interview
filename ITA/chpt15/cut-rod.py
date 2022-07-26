# cut rod into the most revenue made based solution


def cut_rod(p, n):
    r = [0] * (n)
    r[0] = 0
    for i in range(1, n):
        q = float('-inf')
        # print(q)
        for j in range(1, i):
            q = max(q, p[j - 1] + r[i - j])
        r[i] = q
        # print(r[i])

    return r[n]


p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(cut_rod(p, 4))
