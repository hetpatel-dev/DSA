# Binary Search:
# Repeatedly divide a SEARCH SPACE into two parts and eliminate
# the half that cannot contain the answer.

# Basic requirement:
# - The search space must be sorted.

numbers = [2, 5, 8, 12, 16, 23, 38]


def binary_search(arr: list, target: int) -> int:
    """
    Return index of target element in sorted array by repeatedly halving the search space / binary search.

    #### Returns:
        - int: index of the target element
    #### Time Complexity:
        - O(log n): each iteration halves the search space
        - n -> n/2 -> n/4 -> n/8 ......
    #### Space Complexity:
        - O(1)

    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print(binary_search(numbers, 8))   # 2
print(binary_search(numbers, 23))  # 5
print(binary_search(numbers, -10))  # -1, not found
