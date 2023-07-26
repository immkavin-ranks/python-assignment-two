def merge_sort(array, aux_array, start, end):
    if start == end:
        return
    else:
        mid = int((start + end) / 2)
        merge_sort(array, aux_array, start, mid)
        merge_sort(array, aux_array, mid + 1, end)
        merge_both_parts(array, aux_array, start, mid + 1, end)


def merge_both_parts(array, aux_array, left, right, end):
    start = left
    mid = right - 1
    items_count = end - left + 1
    i = 0

    while (left <= mid and right <= end):

        if (array[left] < array[right]):
            aux_array[i] = array[left]
            i += 1
            left += 1

        else:
            aux_array[i] = array[right]
            i += 1
            right += 1

    while left <= mid:
        aux_array[i] = array[left]
        left += 1

    while right <= end:
        aux_array[i] = array[right]
        i += 1
        right += 1

    i = 0

    while i < items_count:
        array[start + i] = aux_array[i]
        i += 1


array = [8, -7, 5, 1, 3, 10, 0]
print("\nInitial array:")
print(array)
merge_sort(array, [0] * (len(array)), 0, len(array) - 1)
print("\nSorted array:")
print(array)
