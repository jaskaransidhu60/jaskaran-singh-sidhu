def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """Rotates the StaticArray by the given steps."""
    n = arr.length()
    result = StaticArray(n)
    steps = steps % n  # Handle large step values
    for i in range(n):
        result.set((i + steps) % n, arr.get(i))
    return result
