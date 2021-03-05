from random import randint
from time import time
import matplotlib.pyplot as plt
from tqdm import tqdm


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
    lst = [3, 6, 2, 8, 1, 10, 4, 5]
    print(insertion_sort(lst))
    # assert selection_sort(lst) == sorted(lst)





if __name__ == '__main__':
    main()


def selection_sort(A):
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
    lst = [3, 6, 2, 8, 1, 10, 4, 5]
    print(selection_sort(lst))
    # assert selection_sort(lst) == sorted(lst)


if __name__ == '__main__':
    main()
