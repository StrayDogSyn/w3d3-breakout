from typing import List

def merge_sort(sequence: List[int]) -> List[int]:
    """
    Recursively sort a list of integers using Merge Sort.
    Time Complexity: O(n log n)
    """
    if len(sequence) <= 1:
        return sequence

    mid = len(sequence) // 2
    left_half = merge_sort(sequence[:mid])
    right_half = merge_sort(sequence[mid:])

    return _merge(left_half, right_half)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted lists into a single sorted list.
    """
    merged = []
    left_idx = right_idx = 0

    # Compare elements one by one and build up the merged list.
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # One of these will be empty—just tack on the remainder.
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged


if __name__ == "__main__":
    my_list = [22, 33, 15, 101, 3, 75, 12, 15, 4, 8]
    sorted_list = merge_sort(my_list)
    print(f"Show me the money, Lebowski! → {sorted_list}")

    new_array = [301, 1982, 158, 23, 15, 42, 777, 369, 4]
    print(f"Make my merge... → {merge_sort(new_array)}")

