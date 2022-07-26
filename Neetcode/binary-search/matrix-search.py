def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    # brute force is O(r*c)
    # you can use binary search on row and column?
    if len(matrix) == 1 and len(matrix[0]) == 1:
        if matrix[0][0] == target:
            return True
        else:
            return False
    r_bottom, r_top, c_right, c_left = len(
        matrix) - 1, 0, len(matrix[0]) - 1, 0
    m = 0
    while r_top <= r_bottom:
        m = r_top + ((r_bottom - 1) // 2)
        # print(m)
        # print(r_bottom, r_top)

        if matrix[m][0] > target:
            r_bottom = m - 1

        elif matrix[m][0] < target:
            r_top = m + 1
        # print(matrix[-1][-1])
        if matrix[m][-1] >= target and matrix[m][0] <= target:
            # print(m)
            # row_num = m
            break

    # print(row_num)

    row = matrix[m]
    # print(row, "row")

    while c_left <= c_right:
        m = c_left + ((c_right - 1)//2)

        if row[m] > target:
            c_right = m - 1

        elif row[m] < target:
            c_left = m + 1
        else:
            return True

    return False


m = [[1, 2, 5, 7], [10, 11, 16, 20], [23, 30, 34, 40]]
m = [[1]]
print(searchMatrix(m, 2))

# NOTE: Dont use while loops seperately
