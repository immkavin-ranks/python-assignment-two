def insertion_sort(array):
    size = len(array)
    i = 1
    while i < size:
        j = i
        temp = array[i]
        while j > 0 and array[j - 1] > temp:
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp
        i += 1


array = [-6, 7, -1, 5, 6, 3, -8]
print("\nInitial array:")
print(array)
insertion_sort(array)
print("\nSorted array:")
print(array)
