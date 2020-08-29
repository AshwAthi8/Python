def findDuplicate(nums):
        nums.sort()
        i=0
        #print(nums)
        while(i<len(nums)-1):
            if(nums[i]==nums[i+1]):
                return nums[i]
                #print(nums[i],end=' ')
                i=i+2
            else:
                i=i+1
#only finds the 1st duplicate
print(findDuplicate([1,2,3,1,-1]))