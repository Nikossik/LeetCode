class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left = 0
        for step in nums:
            if left < 0:
                return False
            elif step > left:
                left = step
            left -= 1
        return True
