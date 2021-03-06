from random import randint
from time import time
import matplotlib.pyplot as plt
from tqdm import tqdm


def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


def RandomLists(num_lst= 5, init_size=10, size_increment=5):
    """
    Generates lists of random numbers

    :param num_lst: number of lists to generate
    :param init_size: initial size of array
    :param size_increment: number by which array is incremented at each step
    :return: random lists
    """
    random_lists = []
    # generating random lists
    for one_list in range(num_lst):
        random_lists.append([])
        for i in range(1,init_size):
            random_lists[one_list].append(randint(1,1000))
        init_size += size_increment
    return random_lists


def SortedLists(num_lst=5, init_size=10, size_increment=5, reverse=False):
    """
    Generates sorted lists

    :param num_lst: number of lists to generate
    :param init_size: initial size of array
    :param size_increment: umber by which array is incremented at each step
    :param reverse: if True generate a list sorted in reverse order
    :return: sorted lists
    """
    sorted_lists= []
    # generating sorted lists
    for one_list in range(num_lst):
        sorted_lists.append([])
        if not reverse:
            for num in range(1, init_size):
                sorted_lists[one_list].append(num)
        else:
            for num in range(init_size,1,-1):
                sorted_lists[one_list].append(num)
        init_size += size_increment
    return sorted_lists


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

    plt.plot(y_bestcase,x_bestcase, color = 'green', label='best case ⊖(n)')
    plt.plot(y_worstcase, x_worstcase, color = 'red', label= 'worst case ⊖($n^2$)')
    plt.plot(y_avg_case,x_avg_case, color='orange', label='average case ⊖($n^2$)')
    plt.title('Time Complexity Insertion Sort')
    plt.legend()
    plt.xlabel('size of arrays')
    plt.ylabel('time (sec)')
    plt.show()

















'''
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
    print("unsorted list:", lst)
    print(f"selection sort:{selection_sort(lst)}")
    # assert selection_sort(lst) == sorted(lst)
    print(f"insertion sort:{insertion_sort(lst)}")
    # assert selection_sort(lst) == sorted(lst)


if __name__ == '__main__':
    main()
'''
