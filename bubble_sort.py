def bubble_sort(array):
    size = len(array)
    i = size - 1
    while i > 0:
        j = 0
        while j < i:
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
            j += 1
        i -= 1


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


array = [-6, 7, -1, 5, 6, 3, -8]
print("\nInitial array:")
print(array)
bubble_sort(array)
print("\nSorted array:")
print(array)