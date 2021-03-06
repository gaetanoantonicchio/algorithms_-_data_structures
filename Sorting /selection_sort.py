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
