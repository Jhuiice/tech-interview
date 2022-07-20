def main():
    arr = [6, 4, 5, 6, 6]
    maxi = max(arr)
    runner_up = 0
    for num in arr:
        if num < maxi and num > runner_up:
            runner_up = num
        print(maxi, runner_up)

    print(runner_up)


main()
