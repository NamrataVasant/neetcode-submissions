class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_seen = []
        for num in nums:
            if num in already_seen:
                return True
            else:
                already_seen += [num] 

        return False
                