def lengthOfLIS(nums):
        n = len(nums)
        if(n==0 or n==1):
            return n&1
        dp = [0]*n
        dp[0] = 1
        maxan = 1
        for i in range(1,n):
            maxval =0
            for j in range(0,i):
                if(nums[i]>nums[j]):
                    maxval = max(maxval,dp[j])
        
            dp[i]=maxval+1
            maxan = max(maxan,dp[i])
        return maxan
print(lengthOfLIS([10,9,2,5,3,7,101,18]))