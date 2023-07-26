def selection_sort(array):
    size = len(array)
    i = 0
    while i < size - 1:
        minimum = i
        j = i + 1
        while j < size:
            if array[j] < array[minimum]:
                minimum = j
            j += 1
        swap(array, minimum, i)
        i += 1


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


array = [-6, 7, -1, 5, 6, 3, -8]
print("\nInitial array:")
print(array)
selection_sort(array)
print("\nSorted array:")
print(array)
