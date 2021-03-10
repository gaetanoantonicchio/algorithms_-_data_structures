#######################
#    MERGE  SORT      #
#######################

def merge_sort(A):
    if len(A) <= 1:
        return A
    midpoint = len(A) // 2

    # split arrays recursively - divide step
    left, right = merge_sort(A[:midpoint]), merge_sort(A[midpoint:])

    return merge_1(A, left, right)  # merge step


def merge_0(left, right):
    """
    Implementation of merge that outputs the result in a new list
    :param left: left half of the array A
    :param right: right half of the array A
    :return: "sorted_list"
    """
    sorted_list = []
    left_pointer, right_pointer = 0, 0

    while left_pointer < len(left) and right_pointer < len(right):

        if left[left_pointer] < right[right_pointer]:
            sorted_list.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_list.append(right[right_pointer])
            right_pointer += 1

    # if there are not elements in one of the arrays
    sorted_list.extend(left[left_pointer:])
    sorted_list.extend(right[right_pointer:])

    return sorted_list


def merge_1(A, left, right):
    """
    Returns a sorted list by overwriting the original unsorted list A
    :param A: original unsorted list
    :param left: left half of the array A
    :param right: right half of the array A
    :return: A sorted
    """
    left_pointer, right_pointer, array_pointer = 0, 0, 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            A[array_pointer] = left[left_pointer]
            left_pointer += 1
            array_pointer += 1

        else:
            A[array_pointer] = right[right_pointer]
            right_pointer += 1
            array_pointer += 1

    if left_pointer == len(left):
        A[array_pointer:] = right[right_pointer:]
    else:
        A[array_pointer:] = left[left_pointer:]
    return A


def main():
    unsorted_list = [4, 6, 2, 1, 8, 3, 9]
    print(merge_sort(unsorted_list))
    assert merge_sort(unsorted_list) == sorted(unsorted_list)


if __name__ == '__main__':
    main()
