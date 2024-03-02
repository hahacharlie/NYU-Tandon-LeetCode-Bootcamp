class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        # pointers one start from the left and one from the right
        left_pointer, right_pointer = 0, len(height) - 1
        # max_area to store the maximum area
        max_area = 0
        
        while left_pointer < right_pointer:
            # Calculate the area with the current left and right
            max_area = max(max_area, min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer))
            # Move the pointer with the smaller height
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return max_area