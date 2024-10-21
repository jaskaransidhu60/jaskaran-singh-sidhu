def reverse(arr: StaticArray) -> None:
    """Reverses the StaticArray in place."""
    left, right = 0, arr.length() - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
