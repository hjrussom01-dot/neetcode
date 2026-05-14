class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = set()
        for x in nums:
            if x not in vals:
                vals.add(x)
            else: return True
        return False