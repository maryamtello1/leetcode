nums=[1,2,3,4,5,6]
#this only works if an array is sorted 

def twoSum(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum==target:
            return [left,right]
        elif sum<target:
            left+=1
        else:
            right-=1

print(twoSum(nums,8))


