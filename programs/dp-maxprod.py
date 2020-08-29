def maxProduct(nums):
        max_end = 1
        min_end = 1
        max_so_far=-100000000000
       
        k = len(nums)
        for i in range(k):
            if(nums[i]>0):
                max_end = max_end*nums[i]
                min_end = min(min_end*nums[i],1)
            
            elif(nums[i]==0):
                max_end=0
                min_end=1
            else:
                t = max_end 
                max_end = min_end*nums[i]
                min_end = t*nums[i]
                
            max_so_far = max(max_so_far,max_end)
            if(max_end<=0):
                max_end=1
        return max_so_far

print(maxProduct([1,0,8,-2,9,-3,-3,7]))