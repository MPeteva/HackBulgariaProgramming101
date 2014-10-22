def is_decreasing(seq):
    if len(seq) == 0:
        return False
    if len(seq) == 1:
        return True

    for i in range(1, len(seq)):
        if seq[i-1] <= seq[i]:
            return False

    return True
