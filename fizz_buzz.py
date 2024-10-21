def fizz_buzz(arr: StaticArray) -> StaticArray:
    """Replaces elements based on divisibility rules."""
    result = StaticArray(arr.length())
    for i in range(arr.length()):
        val = arr.get(i)
        if val % 15 == 0:
            result.set(i, 'fizzbuzz')
        elif val % 3 == 0:
            result.set(i, 'fizz')
        elif val % 5 == 0:
            result.set(i, 'buzz')
        else:
            result.set(i, val)
    return result
