# Linear Search:
# Read elements sequentially from one end to the other and
# inspect each element until the required answer is found
# or the entire collection has been processed.


numbers = [7, 3, 9, 2, 5, 10, 4, 2, 7, 3, 5, 9, 10, 7]


def check_target(arr: list[int], target: int) -> bool:
    """
    Check whether a target exists or not

    #### Returns:
        bool:  
        - True, if target exist
        - False, if target don't exist
    #### Time complexity:
        - O(n) worst case, must process all elements if target is the element or not found
        - O(1) best case, first element is target

    #### Time complexity:
        - O(1), constant

    """
    if not target:
        raise ValueError("Target is compulsory!")
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False


print(check_target(numbers, 10))


def first_occurence(arr: list[int], target: int) -> int | None:
    """
    Return index of the first occurence of target in array.

    #### Returns: 
        - int: index of the first occurence of target
        - None: in case target is not found
    #### Time complexity:
        - O(n) worst case, must process all elements if target is the element or not found
        - O(1) best case, first element is target

    #### Time complexity:
        - O(1), constant
    """
    if not target:
        raise ValueError("Target is compulsory!")
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None


print(first_occurence(numbers, 5))


def last_occurence(arr: list[int], target: int) -> int | None:
    """
    Return index of the last occurence of target in array.

    #### Returns: 
        - int: index of the last occurence of target
        - None: in case target is not found
    #### Time complexity:
        - O(n) worst case, must process all elements if target is the element or not found
        - O(1) best case, last element is target

    #### Time complexity:
        - O(1), constant
    """
    if not target:
        raise ValueError("Target is compulsory!")
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] == target:
            return i
    return None


print(last_occurence(numbers, 5))


def count_total_occurence(arr: list, target: int) -> int:
    """
    Return count of total occurences of the target in array

    #### Returns: 
        - int: total count of the occurences of target
    #### Time complexity:
        - O(n), must process all elements to calculate total count
    #### Time complexity:
        - O(1), constant
    """
    if not target:
        raise ValueError("Target is compulsory!")
    total = 0
    for i in range(0, len(arr)):
        if arr[i] == target:
            total += 1
    return total


print(count_total_occurence(numbers, 7))


def find_all_occurence(arr: list, target: int) -> list[int]:
    """
    Return collection of all indexes where target is present in array.

    #### Returns:
        - list[int]: list of all indexes where target is present
    #### Time Complexity:
        - O(n): process all n elements
    #### Space Complextiy:
        - O(k): k is the number of indexes
    """

    if not target:
        raise ValueError("Target is compulsory!")
    indexes = []
    for i in range(len(arr)):
        if arr[i] == target:
            indexes.append(i)
    return indexes


print(find_all_occurence(numbers, 7))
print(find_all_occurence(numbers, 7))
