def intersection(nums1,nums2):
        nums1.sort()
        nums2.sort()
        l1 = len(nums1)
        l2 = len(nums2)
        i = 0
        j = 0
        c = []
        while(i<l1 and j < l2):
            if(nums1[i] == nums2[j]):
                if nums1[i] not in c:
                    c.append(nums1[i])
                i=i+1
                j=j+1
            elif(nums1[i]>nums2[j]):
                j=j+1
            else:
                i=i+1
                
        return (c)
print(intersection([1,2,4,5,2],[2,5,3]))