def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = merge_sort(string[:mid])
    right = merge_sort(string[mid:])

    return merge(string, left, right)


def merge(string_merged, left, right):
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            string_merged[left_idx + right_idx] = left[left_idx]
            left_idx += 1
        else:
            string_merged[left_idx + right_idx] = right[right_idx]
            right_idx += 1

    for left_idx in range(left_idx, len(left)):
        string_merged[left_idx + right_idx] = left[left_idx]

    for right_idx in range(right_idx, len(right)):
        string_merged[left_idx + right_idx] = right[right_idx]

    return string_merged


def is_anagram(first_string, second_string):

    first_ordened = ''
    second_ordened = ''

    for letter in merge_sort(list(first_string.lower())):
        first_ordened += letter
    for letter in merge_sort(list(second_string.lower())):
        second_ordened += letter

    return (
        first_ordened,
        second_ordened,
        True if first_ordened == second_ordened and
        len(first_ordened) > 0 and len(first_ordened) > 0 else False
    )
