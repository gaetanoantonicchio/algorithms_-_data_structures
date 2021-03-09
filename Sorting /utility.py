from random import randint
from time import time
import matplotlib.pyplot as plt
from insertion_sort import *
from selection_sort import *


def RandomLists(num_lst=5, init_size=10, size_increment=5):
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
        for i in range(1, init_size):
            random_lists[one_list].append(randint(1, 1000))
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
    sorted_lists = []
    # generating sorted lists
    for one_list in range(num_lst):
        sorted_lists.append([])
        if not reverse:
            for num in range(1, init_size):
                sorted_lists[one_list].append(num)
        else:
            for num in range(init_size, 1, -1):
                sorted_lists[one_list].append(num)
        init_size += size_increment
    return sorted_lists


def compare_IS_SS(arrays, case):
    avail_case = 'best', 'worst', 'avg'
    x_bestcase_algo1, x_avg_case_algo1, x_worstcase_algo1 = [], [], []
    x_bestcase_algo2, x_avg_case_algo2, x_worstcase_algo2 = [], [], []
    y_size = []

    if case not in avail_case:
        raise ValueError(f"case should be one among :{avail_case}")

    if case == 'best':
        for list in arrays:
            start = time()
            insertion_sort(list)
            elapsed = time() - start
            x_bestcase_algo1.append(elapsed)
            y_size.append(len(list))
            start = time()
            selection_sort(list)
            elapsed = time() - start
            x_bestcase_algo2.append(elapsed)

        plt.plot(y_size, x_bestcase_algo1, color='green', label='best case IS')
        plt.plot(y_size, x_bestcase_algo2, color='blue', label='best case SS')
        plt.title(f"Time Complexity Insertion Sort vs Selection Sort")
        plt.legend()
        plt.xlabel('size of arrays')
        plt.ylabel('time (sec)')
        plt.show()

    elif case == 'worst':
        for list in arrays:
            start = time()
            insertion_sort(list)
            elapsed = time() - start
            x_worstcase_algo1.append(elapsed)
            y_size.append(len(list))
            start = time()
            selection_sort(list)
            elapsed = time() - start
            x_worstcase_algo2.append(elapsed)

        plt.plot(y_size, x_worstcase_algo1, color='red', label='worst case IS')
        plt.plot(y_size, x_worstcase_algo2, color='blue', label='worst case SS')
        plt.title(f"Time Complexity Insertion Sort vs Selection Sort")
        plt.legend()
        plt.xlabel('size of arrays')
        plt.ylabel('time (sec)')
        plt.show()

    else:
        for list in arrays:
            start = time()
            insertion_sort(list)
            elapsed = time() - start
            x_avg_case_algo1.append(elapsed)
            y_size.append(len(list))
            start = time()
            selection_sort(list)
            elapsed = time() - start
            x_avg_case_algo2.append(elapsed)

        plt.plot(y_size, x_avg_case_algo1, color='red', label='avg case IS')
        plt.plot(y_size, x_avg_case_algo2, color='blue', label='avg case SS')
        plt.title(f"Time Complexity Insertion Sort vs Selection Sort")
        plt.legend()
        plt.xlabel('size of arrays')
        plt.ylabel('time (sec)')
        plt.show()


def main():
    unsorted_lists = RandomLists(num_lst=40, init_size=100, size_increment=100)
    print(compare_IS_SS(unsorted_lists, case='avg'))


if __name__ == '__main__':
    main()
