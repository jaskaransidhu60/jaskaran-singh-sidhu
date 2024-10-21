def count_sort(arr):
    """Sorts the StaticArray using count sort."""
    min_val, max_val = min_max(arr)
    range_size = max_val - min_val + 1
    count = [0] * range_size
    result = StaticArray(arr.length())
    for i in range(arr.length()):
        count[arr.get(i) - min_val] += 1
    index = 0
    for i in range(range_size - 1, -1, -1):
        while count[i] > 0:
            result.set(index, i + min_val)
            index += 1
            count[i] -= 1
    return result
