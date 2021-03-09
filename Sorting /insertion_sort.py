from time import time
import matplotlib.pyplot as plt

########################
#    INSERTION SORT    #
########################


def insertion_sort(A=[]):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

########################################
#   INSERTION SORT - COMPLEXITY TEST   #
########################################

def test_IS(sort_lists, rev_sort_lists, random_lists):
    x_bestcase = []
    y_bestcase = []
    x_avg_case = []
    y_avg_case = []
    x_worstcase = []
    y_worstcase = []

    for list in sort_lists:
        start = time()
        insertion_sort(list)
        elapsed = time() - start
        x_bestcase.append(elapsed)
        y_bestcase.append(len(list))

    for list in rev_sort_lists:
        start = time()
        insertion_sort(list)
        elapsed = time() - start
        x_worstcase.append(elapsed)
        y_worstcase.append(len(list))

    for list in random_lists:
        start = time()
        insertion_sort(list)
        elapsed = time() - start
        x_avg_case.append(elapsed)
        y_avg_case.append(len(list))

    plt.plot(y_bestcase, x_bestcase, color='green', label='best case ⊖(n)')
    plt.plot(y_worstcase, x_worstcase, color='red', label='worst case ⊖($n^2$)')
    plt.plot(y_avg_case, x_avg_case, color='orange', label='average case ⊖($n^2$)')
    plt.title('Time Complexity Insertion Sort')
    plt.legend()
    plt.xlabel('size of arrays')
    plt.ylabel('time (sec)')
    plt.show()


def main():
    lst = [3, 6, 2, 8, 1, 10, 4, 5]
    print("unsorted list:", lst)
    assert insertion_sort(lst) == sorted(lst)
    print(f"insertion sort:{insertion_sort(lst)}")


if __name__ == '__main__':
    main()
