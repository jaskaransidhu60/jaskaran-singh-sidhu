def rotate(arr, steps):
    """Returns a new StaticArray with elements rotated by the given number of steps."""
    n = arr.length()
    result = StaticArray(n)
    steps = steps % n  # Handle large step values
    for i in range(n):
        result.set((i + steps) % n, arr.get(i))
    return result
