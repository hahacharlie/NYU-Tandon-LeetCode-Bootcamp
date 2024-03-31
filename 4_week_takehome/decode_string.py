class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # To keep track of strings and numbers
        currentNum = 0
        currentString = ''
        for c in s:
            if c.isdigit():
                currentNum = currentNum * 10 + int(c)  # Build the current number (could be more than one digit)
            elif c == '[':
                # Push the current number and string onto the stack (save the state)
                stack.append((currentString, currentNum))
                # Reset for the new string inside brackets
                currentString, currentNum = '', 0
            elif c == ']':
                # Pop the last string and number, and decode the current encoded string
                lastString, num = stack.pop()
                currentString = lastString + currentString * num
            else:
                # Build the current string
                currentString += c
        return currentString