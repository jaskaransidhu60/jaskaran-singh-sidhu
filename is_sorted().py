def is_sorted(arr: StaticArray) -> int:
    """Checks if the array is sorted in ascending or descending order."""
    ascending = descending = True
    for i in range(1, arr.length()):
        if arr.get(i) < arr.get(i - 1):
            ascending = False
        if arr.get(i) > arr.get(i - 1):
            descending = False
    if ascending:
        return 1
    elif descending:
        return -1
    else:
        return 0
