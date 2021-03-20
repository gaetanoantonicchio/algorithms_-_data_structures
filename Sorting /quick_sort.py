#################################
#         Quick Sort            #
#################################

list1 = [2, 5, 1, 8, 4, 6, 9, 3, 7]

def partition(A, p, r):
    pivot = A[r]
    i= p-1
    
    for j in range(p,r):
        if A[j]<= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1  #index of pivot 


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)
    return A

        
def main():
    print(quick_sort(list1, 0, len(list1)-1))

if __name__ == '__main__':
    main()