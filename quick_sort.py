# Quick sort algorithm implementation

from typing import List, Tuple
import random
import time


def partition(arr: List[int], low: int, high: int) -> int:
    """
    Partition function for quicksort that arranges elements around a pivot.
    
    Args:
        arr: The array to be partitioned
        low: Starting index of the partition
        high: Ending index of the partition
        
    Returns:
        The pivot index after partitioning
    """
    # Choose the rightmost element as the pivot
    pivot = arr[high]
    
    # Index of the smaller element
    i = low - 1
    
    # Iterate through the sub-array
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            # Increment the index of the smaller element
            i += 1
            # Swap the current element with the element at index i
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place the pivot element at its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the pivot index
    return i + 1


def quick_sort(arr: List[int], low: int, high: int) -> None:
    """
    Recursive quicksort function that sorts an array in-place.
    
    Args:
        arr: The array to be sorted
        low: Starting index of the array
        high: Ending index of the array
    """
    # Base case: If the partition has one element or less, it's already sorted
    if low < high:
        # Find the pivot index such that all elements to the left are smaller
        # and all elements to the right are greater
        pi = partition(arr, low, high)
        
        # Recursively sort the sub-arrays
        quick_sort(arr, low, pi - 1)    # Left partition
        quick_sort(arr, pi + 1, high)   # Right partition


def randomized_partition(arr: List[int], low: int, high: int) -> int:
    """
    Randomized partition function that selects a random pivot to improve
    average-case performance and avoid worst-case scenarios.
    
    Args:
        arr: The array to be partitioned
        low: Starting index of the partition
        high: Ending index of the partition
        
    Returns:
        The pivot index after partitioning
    """
    # Choose a random pivot and swap with the rightmost element
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    
    # Call the standard partition function
    return partition(arr, low, high)


def randomized_quick_sort(arr: List[int], low: int, high: int) -> None:
    """
    Randomized version of quicksort for better average performance.
    
    Args:
        arr: The array to be sorted
        low: Starting index of the array
        high: Ending index of the array
    """
    if low < high:
        # Get partition index using randomized pivot
        pi = randomized_partition(arr, low, high)
        
        # Recursively sort the sub-arrays
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)


def time_quicksort(arr: List[int]) -> Tuple[float, List[int]]:
    """
    Time the execution of quicksort and return the sorted array.
    
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
    quick_sort(arr_copy, 0, len(arr_copy) - 1)
    
    # Record end time
    end_time = time.time()
    
    return end_time - start_time, arr_copy


# Example usage
if __name__ == "__main__":
    # Test with a random array
    test_array = [random.randint(1, 1000) for _ in range(20)]
    
    print("Original array:", test_array)
    
    # Sort using standard quicksort
    execution_time, sorted_array = time_quicksort(test_array)
    
    print("Sorted array:", sorted_array)
    print(f"Sorting took {execution_time:.6f} seconds")
    
    # Verify the sorting is correct
    assert sorted_array == sorted(test_array), "Sorting failed!"
    
    print("Sorting verified correctly!")
    
    # Compare with randomized quicksort
    test_array_2 = test_array.copy()
    start = time.time()
    randomized_quick_sort(test_array_2, 0, len(test_array_2) - 1)
    end = time.time()
    
    print(f"Randomized quicksort took {end - start:.6f} seconds")
    print("Both implementations give the same result:", test_array_2 == sorted_array)

