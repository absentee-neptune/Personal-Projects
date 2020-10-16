def squareEach(nums):
    for ctr in range(len(nums)):
        nums[ctr] **= 2
    return nums        
 
def squareEachNew(nums):
    newList = []
    for num in nums:
        newList.append(num**2)
    return newList

nums = [1,2,3,4,5]
print(squareEachNew(nums))
