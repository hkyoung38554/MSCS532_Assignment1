def insertion_sort_desc(arr):
    """
    Sorts a list in-place in monotonically decreasing order using the insertion sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    nums = [6, 3, 10, 2, 5]
    print("Original list:", nums)
    sorted_list = insertion_sort_desc(nums)
    print("Sorted list(monotonically decreasing):", sorted_list)
