# #to use binary search your array has to be sorted
# #runtime of binary search: O(log n)
# it's faster than linear search, which has a time complexity of O(n)

arr = [5,3,6,7,8,10]
sortedArr= sorted(arr)


def binarySearch(arr,target):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            start=mid+1
        else:
            end = mid-1
    #if nothing is found return -1
    return -1

print(binarySearch(arr,10))

    

