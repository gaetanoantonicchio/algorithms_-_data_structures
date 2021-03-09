#######################
#    MERGE  SORT      #
#######################

def merge_sort(A):
    if len(A) <= 1:
        return A
    midpoint = len(A) // 2

    # split arrays recursively - divide step
    left, right = merge_sort(A[:midpoint]), merge_sort(A[midpoint:])

    return merge(left, right)  # merge step


def merge(left, right):
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


def main():
    unsorted_list = [4, 6, 2, 1, 8, 3, 9]
    print(merge_sort(unsorted_list))
    assert merge_sort(unsorted_list) == sorted(unsorted_list)


if __name__ == '__main__':
    main()
