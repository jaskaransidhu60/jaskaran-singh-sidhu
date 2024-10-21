def sa_range(start: int, end: int) -> StaticArray:
    """Creates a StaticArray with all integers between start and end."""
    length = abs(end - start) + 1
    result = StaticArray(length)
    step = 1 if start <= end else -1
    for i in range(length):
        result.set(i, start + i * step)
    return result
