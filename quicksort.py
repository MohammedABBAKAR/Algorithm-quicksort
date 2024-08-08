def quicksort(array): 
    if len(array) < 2:
        return array 
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater) 
print (quicksort([10, 5, 2, 3]))

# Code Explanation:
# 1 Base Case:

# if len(array) < 2:
#     return array

# If the array has one element or is empty, it is already sorted, so return the array as is.

# 2 Choosing the Pivot:

# pivot = array[0]
# Select the first element of the array as the pivot.


# 3 Partitioning the Array:
# less = [i for i in array[1:] if i <= pivot]
# greater = [i for i in array[1:] if i > pivot]


# less: Contains all elements from the array that are less than or equal to the pivot.
# greater: Contains all elements from the array that are greater than the pivot.

# 4 Recursive Call:

# return quicksort(less) + [pivot] + quicksort(greater)

# Recursively apply the quicksort function on the less and greater subarrays, then concatenate the sorted less array, 
# the pivot, and the sorted greater array to get the fully sorted array.