#This is the algo to find the Largest sum of contiguous subarray;
#works for negative numbers

def maxSubArray(nums):
        max_so_far = -10000000000000000
        max_end_here = 0
        for i in range(len(nums)):
            max_end_here = max_end_here + nums[i]
            if(max_end_here > max_so_far):
                max_so_far = max_end_here
            if(max_end_here < 0):
                max_end_here =0
        if(max_so_far==0):
            return max(nums)
        return max_so_far

print(maxSubArray([1,3,4,0]))