def get_slices(sequence, length):
    sequence_len = len(sequence)
    if length < 1:
        raise ValueError('The length cannot be less than 1.')
    if sequence_len < length:
        raise ValueError('The length cannot be greater than sequence.')
    slices = [sequence[0+i:i+length] for i in range(sequence_len) if i + length <= sequence_len]
    return slices
