def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i in nums:
            dp.append(i)
        for i in range(1,len(nums)):
            for j in range(i):
                if(nums[i]>nums[j] and dp[i]<dp[j]+nums[i]):
                    dp[i]=dp[j]+nums[i]
        return max(dp)