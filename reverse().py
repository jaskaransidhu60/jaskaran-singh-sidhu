def reverse(arr):
    """Reverses the StaticArray in-place."""
    left, right = 0, arr.length() - 1
    while left < right:
        arr.set(left, arr.get(left) ^ arr.get(right))
        arr.set(right, arr.get(left) ^ arr.get(right))
        arr.set(left, arr.get(left) ^ arr.get(right))
        left += 1
        right -= 1
