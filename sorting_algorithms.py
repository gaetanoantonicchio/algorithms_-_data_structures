def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


def main():
    list = [3, 6, 2, 8, 1, 10, 4, 5]
    print(insertion_sort(list))
    assert insertion_sort(list) == sorted(list)


if __name__ == '__main__':
    main()
