'''
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map_vals = {}
        nums = sorted(nums)
        for i in nums:
            if i in map_vals:
                return True
            map_vals[i] = map_vals.get(i,0) + 1
        return False

if __name__ == '__main__':
    print(Solution().containsDuplicate([1,2,3,4]))