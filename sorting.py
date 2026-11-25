def merge_sort_parcels(parcels):
    """
    Sort parcels by:
    1. Higher priority first
    2. Earlier deadline first when priorities are equal

    This is Merge Sort. It returns a new sorted list.
    """
    if len(parcels) <= 1:
        return parcels

    middle = len(parcels) // 2
    left = merge_sort_parcels(parcels[:middle])
    right = merge_sort_parcels(parcels[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        left_key = (-left[i]["priority"], left[i]["deadline"])
        right_key = (-right[j]["priority"], right[j]["deadline"])

        if left_key <= right_key:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
