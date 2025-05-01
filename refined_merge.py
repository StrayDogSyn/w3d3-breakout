# Merge sort algorithm implementation

from typing import List, Tuple
import time
import random


def merge_sort(sequence: List[int]) -> List[int]:
    """
    Recursively sort a list of integers using Merge Sort.
    
    Merge sort is a divide-and-conquer algorithm that:
    1. Divides the input array into two halves
    2. Recursively sorts the two halves
    3. Merges the two sorted halves to produce a single sorted array
    
    Args:
        sequence: The list to be sorted
        
    Returns:
        A new sorted list containing the same elements as the input
        
    Time Complexity: O(n log n) - consistent performance regardless of input data
    Space Complexity: O(n) - requires additional space proportional to input size
    """
    # Base case: Lists of size 0 or 1 are already sorted
    if len(sequence) <= 1:
        return sequence

    # Divide the list into two halves
    mid = len(sequence) // 2
    
    # Recursively sort both halves
    left_half = merge_sort(sequence[:mid])
    right_half = merge_sort(sequence[mid:])

    # Merge the sorted halves
    return _merge(left_half, right_half)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted lists into a single sorted list.
    
    This is the key operation in merge sort where two already-sorted lists
    are combined to form a new sorted list in linear time.
    
    Args:
        left: The first sorted list
        right: The second sorted list
        
    Returns:
        A new sorted list containing all elements from both input lists
    """
    merged = []
    left_idx = right_idx = 0

    # Compare elements one by one and build up the merged list
    while left_idx < len(left) and right_idx < len(right):
        # Choose the smaller of the two current elements
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # At this point, one of the lists has been fully processed
    # Append any remaining elements from the unfinished list
    # (Only one of these will actually append elements)
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return merged


def optimized_merge_sort(sequence: List[int]) -> List[int]:
    """
    An optimized version of merge sort that uses insertion sort for small subarrays.
    
    For very small arrays, the overhead of recursion may outweigh the benefits of
    merge sort's optimal time complexity. Using insertion sort for small subarrays
    can improve overall performance.
    
    Args:
        sequence: The list to be sorted
        
    Returns:
        A new sorted list containing the same elements as the input
    """
    # Use regular merge sort for the interface
    return _optimized_merge_sort(sequence.copy(), 0, len(sequence))


def _optimized_merge_sort(arr: List[int], start: int, end: int) -> List[int]:
    """
    Helper function for the optimized merge sort implementation.
    
    Args:
        arr: The list being sorted
        start: Start index of the current subarray
        end: End index (exclusive) of the current subarray
        
    Returns:
        The sorted list
    """
    # Small array optimization: use insertion sort for small subarrays
    if end - start <= 10:  # Threshold can be tuned
        _insertion_sort(arr, start, end)
        return arr
    
    # Regular merge sort for larger arrays
    mid = start + (end - start) // 2
    _optimized_merge_sort(arr, start, mid)
    _optimized_merge_sort(arr, mid, end)
    
    # Merge the two sorted halves
    _merge_in_place(arr, start, mid, end)
    return arr


def _insertion_sort(arr: List[int], start: int, end: int) -> None:
    """
    Sort a small subarray using insertion sort.
    
    Args:
        arr: The array containing the subarray to be sorted
        start: The starting index of the subarray
        end: The ending index (exclusive) of the subarray
    """
    for i in range(start + 1, end):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def _merge_in_place(arr: List[int], start: int, mid: int, end: int) -> None:
    """
    Merge two sorted subarrays in-place.
    
    Args:
        arr: The array containing the subarrays to be merged
        start: Start index of the first subarray
        mid: End index of the first subarray and start of the second
        end: End index of the second subarray
    """
    # Create temporary copies of the subarrays
    left = arr[start:mid]
    right = arr[mid:end]
    
    # Merge back into arr[start:end]
    left_idx = right_idx = 0
    dest_idx = start
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            arr[dest_idx] = left[left_idx]
            left_idx += 1
        else:
            arr[dest_idx] = right[right_idx]
            right_idx += 1
        dest_idx += 1
    
    # Copy any remaining elements
    while left_idx < len(left):
        arr[dest_idx] = left[left_idx]
        left_idx += 1
        dest_idx += 1
        
    while right_idx < len(right):
        arr[dest_idx] = right[right_idx]
        right_idx += 1
        dest_idx += 1


def time_merge_sort(arr: List[int]) -> Tuple[float, List[int]]:
    """
    Time the execution of merge sort and return the sorted array.
    
    Args:
        arr: The array to be sorted
        
    Returns:
        Tuple of (execution_time_in_seconds, sorted_array)
    """
    # Create a copy to avoid modifying the original
    arr_copy = arr.copy()
    
    # Record start time
    start_time = time.time()
    
    # Sort the array
    sorted_arr = merge_sort(arr_copy)
    
    # Record end time
    end_time = time.time()
    
    return end_time - start_time, sorted_arr


if __name__ == "__main__":
    # Test with a defined array
    my_list = [22, 33, 15, 101, 3, 75, 12, 15, 4, 8]
    print("Original array:", my_list)
    
    # Time and perform regular merge sort
    execution_time, sorted_list = time_merge_sort(my_list)
    print(f"Sorted array: {sorted_list}")
    print(f"Merge sort took {execution_time:.6f} seconds")
    
    # Verify the sorting is correct
    assert sorted_list == sorted(my_list), "Sorting failed!"
    print("Sorting verified correctly!")
    
    # Test with another array
    new_array = [301, 1982, 158, 23, 15, 42, 777, 369, 4]
    print("\nSecond test array:", new_array)
    
    # Time and sort with optimized version
    start = time.time()
    optimized_result = optimized_merge_sort(new_array)
    end = time.time()
    
    print(f"Optimized sorted result: {optimized_result}")
    print(f"Optimized merge sort took {end - start:.6f} seconds")
    print("Correct sorting:", optimized_result == sorted(new_array))
    
    # Compare with standard merge sort for longer array
    print("\nPerformance comparison with larger array:")
    large_array = [random.randint(1, 10000) for _ in range(1000)]
    
    # Standard merge sort
    std_time, std_result = time_merge_sort(large_array)
    print(f"Standard merge sort: {std_time:.6f} seconds")
    
    # Optimized merge sort
    opt_start = time.time()
    opt_result = optimized_merge_sort(large_array)
    opt_time = time.time() - opt_start
    print(f"Optimized merge sort: {opt_time:.6f} seconds")
    
    print(f"Both implementations give the same result: {std_result == opt_result}")

