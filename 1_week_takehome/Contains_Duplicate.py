'''
Problem: Given an integer array nums, return true if any value appears at least twice in the array, 
        and return false if every element is distinct.
'''
# this is the simplest way to do it, but it is not the most efficient
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                return True
        return False

# this is the most efficient way to do it (I can think of at least)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        A set() function in Python is an unordered collection of unique elements. 
        When a list is converted to a set, any duplicate elements in the list are removed. 
        Therefore, if the length of the set is less than the length of the original list, 
        it means that there were duplicate elements in the list.
        '''
        return len(set(nums)) != len(nums)