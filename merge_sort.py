def merge_sort(array, aux_array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(array, aux_array, start, mid)
        merge_sort(array, aux_array, mid + 1, end)
        merge_both_parts(array, aux_array, start, mid, end)

def merge_both_parts(array, aux_array, left, mid, end):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= end:
        if array[i] <= array[j]:
            aux_array[k] = array[i]
            i += 1
        else:
            aux_array[k] = array[j]
            j += 1
        k += 1

    while i <= mid:
        aux_array[k] = array[i]
        i += 1
        k += 1

    while j <= end:
        aux_array[k] = array[j]
        j += 1
        k += 1

    for k in range(left, end + 1):
        array[k] = aux_array[k]

array = [8, -7, 5, 1, 3, 10, 0]
aux_array = [0] * len(array)
print("Initial array:")
print(array)
merge_sort(array, aux_array, 0, len(array) - 1)
print("Sorted array:")
print(array)
