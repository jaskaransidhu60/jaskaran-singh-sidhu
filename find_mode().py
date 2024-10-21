def find_mode(arr):
    """Finds the mode and its frequency."""
    mode, mode_count = arr.get(0), 1
    current_count = 1
    for i in range(1, arr.length()):
        if arr.get(i) == arr.get(i - 1):
            current_count += 1
        else:
            if current_count > mode_count:
                mode, mode_count = arr.get(i - 1), current_count
            current_count = 1
    if current_count > mode_count:
        mode, mode_count = arr.get(arr.length() - 1), current_count
    return mode, mode_count
