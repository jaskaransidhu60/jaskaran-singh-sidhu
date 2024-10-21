def remove_duplicates(arr):
    """Removes duplicates from a sorted StaticArray."""
    result = StaticArray(arr.length())
    result.set(0, arr.get(0))
    j = 1
    for i in range(1, arr.length()):
        if arr.get(i) != arr.get(i - 1):
            result.set(j, arr.get(i))
            j += 1
    return StaticArray(j)
