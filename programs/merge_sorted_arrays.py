def merge(nums1, m , nums2 ,n):
        for i in range(n):
            j=m-1+i
            while(j>=0 and nums1[j]>nums2[i]):
                nums1[j+1]=nums1[j]
                j=j-1
            nums1[j+1]=nums2[i]
        return nums1
print(merge([2,4,9,0,0,0],3,[0,4,10],3))