def subsetOR(arr, l, r, bsum=0):
    if l > r:
        sum_arr.append(bsum)
        return

    subsetOR(arr, l + 1, r, bsum | arr[l])

    subsetOR(arr, l + 1, r, bsum)


if __name__ == '__main__':

    t = int(raw_input().strip())

    for a0 in range(t):
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        sum_arr = []
        subsetOR(arr, 0, n-1)
        print(sum(sum_arr))