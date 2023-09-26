left = [1, 4, 7]
right = [2, 5, 6]

def merge(left, right):
    result = []  # Create an empty list to store the merged result
    i=0
    j=0  # Initialize pointers for the left and right arrays

    # Compare elements from both arrays and add the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # After the loop, one of the arrays may have some elements left.
    # Extend the result with the remaining elements from both arrays.
    result.extend(left[i:])
    result.extend(right[j:])

    return result  # Return the merged and sorted result

print(merge(left,right))