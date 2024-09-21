import main


# use quicksort via recursion
def quickSort(arr):
    # if the array has one or less elements then return the array
    if len(arr) <= 1:
        return arr

    # find the pivot which in this case is the middle value
    pivot = arr[len(arr) // 2]

    # sets the left side of the list (this is the side that has values smaller than the pivot value )
    left = [x for x in arr if x < pivot]

    # sets the middle array. this is the array that is already sorted as it only contains the pivot value
    middle = [x for x in arr if x == pivot]

    # sets the right side of the array (this is the side that has values larger than the pivot value)
    right = [x for x in arr if x > pivot]

    # recursively sorts the left side of the array and the right side of the array and combines the array
    return quickSort(left) + middle + quickSort(right)
