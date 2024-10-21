def fizz_buzz(arr):
    """Returns a new StaticArray with 'fizz', 'buzz', or 'fizzbuzz' replacing certain values."""
    result = StaticArray(arr.length())
    for i in range(arr.length()):
        value = arr.get(i)
        if value % 15 == 0:
            result.set(i, 'fizzbuzz')
        elif value % 3 == 0:
            result.set(i, 'fizz')
        elif value % 5 == 0:
            result.set(i, 'buzz')
        else:
            result.set(i, value)
    return result
