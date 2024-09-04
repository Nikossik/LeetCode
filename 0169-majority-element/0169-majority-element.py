from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        r = sorted(cnt.items(), key=lambda x: x[1], reverse=True)[0]
        if r[1] > len(nums)/2:
            return r[0]
        