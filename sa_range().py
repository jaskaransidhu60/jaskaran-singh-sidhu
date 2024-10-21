def sa_range(start, end):
    """Creates a StaticArray with all integers from start to end inclusive."""
    length = abs(end - start) + 1
    result = StaticArray(length)
    step = 1 if start <= end else -1
    for i in range(length):
        result.set(i, start + i * step)
    return result
