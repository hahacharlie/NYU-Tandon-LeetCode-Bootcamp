class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to keep track of character counts within the window
        char_count = {}
        max_length = 0
        left = 0
    
        for right in range(len(s)):
            # Add current character to the count
            char_count[s[right]] = char_count.get(s[right], 0) + 1
        
            # Check if the current window is valid (window size - max character count <= k)
            while (right - left + 1) - max(char_count.values()) > k:
                # If not valid, move left pointer to shrink the window
                char_count[s[left]] -= 1
                left += 1
            
            # Update max_length if the current window is larger
            max_length = max(max_length, right - left + 1)
    
        return max_length