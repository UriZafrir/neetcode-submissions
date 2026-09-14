class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Key: the number, Value: its most recent index
        seen = {}

        for i, num in enumerate(nums):
            # If we've seen this number before AND it's within distance k
            if num in seen and i - seen[num] <= k:
                return True

            # Update the dictionary with the current index of the number
            seen[num] = i

        return False