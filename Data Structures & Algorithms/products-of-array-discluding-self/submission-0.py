class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1=nums
        nums2=[]
        n=len(nums)
        prod=1
        for i in range(n):
            for j in range(n):
                if j==i:
                    pass
                else:
                    prod*=nums1[j]
            nums2.append(prod)
            prod=1
        return nums2