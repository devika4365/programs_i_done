class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i=0
        s=[]
        n=len(nums)
        while i<n:
            k=[nums[i+1] for j in range(nums[i])]
            s.extend(k)
            i=i+2
        return s
            
