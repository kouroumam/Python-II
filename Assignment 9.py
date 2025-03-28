

def merge_sort(names):
    if len(names) <= 1:
        return names  # Already sorted if only one name

    # Split list into two halves
    mid = len(names) // 2
    left = merge_sort(names[:mid])
    right = merge_sort(names[mid:])

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))

    return sorted_list + left + right  # Add remaining items

# Example usage
names = ["brandy", "april", "danielle", "cheryl"]
print(merge_sort(names))  