class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen={}
        n=len(numbers)
        i=0
        while numbers[i]+numbers[n-1]!= target:
            if numbers[i]+numbers[n-1]>target:
                n=n-1
            elif numbers[i]+numbers[n-1]<target:
                i=i+1
        return [i+1,n]