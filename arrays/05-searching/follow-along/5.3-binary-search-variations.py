# precondition: array must be sorted

def first_occurence_binary_search(arr: list, target: int) -> int:
    """
    Return the index of the first/leftmost occurence of given target.

    #### Precondition:
        - array must be sorted.

    #### Returns:
        - int: index of the first occurence of target element.

    #### Time Complexity:
        - O(log n): where n is the number of elements of array.
        - each iteration havles the search space, such as n -> n/2 -> n/4...

    #### Space Complexity:
        - O(1)
    """

    left, right = 0, len(arr) - 1
    ans = None

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans


print(first_occurence_binary_search(
    [1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7, 8, 9], 4))


def last_occurence_binary_search(arr: list, target: int) -> int:
    """
    Return the index of the last/rightmost occurence of given target.

    #### Precondition:
        - array must be sorted.

    #### Returns:
        - int: index of the last occurence of target element.

    #### Time Complexity:
        - O(log n): where n is the number of elements of array.
        - each iteration havles the search space, such as n -> n/2 -> n/4...

    #### Space Complexity:
        - O(1)
    """
    left, right = 0, len(arr) - 1
    ans = None

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            ans = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = right - 1

    return ans


print(last_occurence_binary_search(
    [1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7, 8, 9], 4))
