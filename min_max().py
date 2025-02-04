def min_max(arr: StaticArray) -> tuple[int, int]:
    """Returns the minimum and maximum values of the StaticArray."""
    min_val = max_val = arr.get(0)  # Initialize with the first element
    for i in range(1, arr.length()):
        val = arr.get(i)
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val
    return min_val, max_val
