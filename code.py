class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)

        c=0
        a,b=-1,-1
        ans=[a,b]
        for i in range(n):
            if nums[i]==target :
                c+=1
                if c==1:
                    a=i
                    ans=[a,b]
                else :
                    ans=[a,i]
        if c==1:
            return [a,a]

        return ans
        
