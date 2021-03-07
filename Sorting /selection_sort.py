from utility import *


def selection_sort(A=[]):
    for j in range(len(A)):
        min_index = j
        for i in range(j + 1, len(A)):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if A[i] < A[min_index]:
                min_index = i
        A[j], A[min_index] = A[min_index], A[j]
    return A


def main():
    array = [3, 1, 8, 45, 9, 20, 37]
    print(selection_sort(array))
    assert selection_sort(array) == sorted(array)


if __name__ == '__main__':
    main()


