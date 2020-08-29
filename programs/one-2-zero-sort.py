def sortColors(nums):
        m = 0
        h = len(nums)-1
        l = 0
        while(m<=h):
            if(nums[m]==0):
                nums[m],nums[l]=nums[l],nums[m]
                l=l+1
                m=m+1
            elif(nums[m]==1):
                m=m+1
            else:
                nums[m],nums[h]=nums[h],nums[m]
                h=h-1
        return nums
         #dont have to increment m here as the value swapped can be 0 or 1 which needs to be sorted.

print(sortColors([1,0,0,1,2,2,1,1,0]))