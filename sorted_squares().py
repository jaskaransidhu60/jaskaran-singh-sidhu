def sorted_squares(arr: StaticArray) -> StaticArray:
    """Returns a StaticArray with squares of elements sorted."""
    n = arr.length()
    result = StaticArray(n)
    left, right, index = 0, n - 1, n - 1
    while left <= right:
        left_square = arr.get(left) ** 2
        right_square = arr.get(right) ** 2
        if left_square > right_square:
            result.set(index, left_square)
            left += 1
        else:
            result.set(index, right_square)
            right -= 1
        index -= 1
    return result
