class Solution:
    def myAtoi(self, s: str) -> int:
        # reading and ignore any leading whitespace
        s = s.strip()
        if not s:
            return 0

        # check if the first character is a sign
        sign = -1 if s[0] == '-' else 1
        if s[0] in ['-', '+']:
            s = s[1:]

        # Read in next the characters until the next non-digit character
        # or the end of the input is reached. The rest of the string is ignored.
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        # Check for overflow and return INT_MAX or INT_MIN
        if result > (2 ** 31 - 1):
            return (2 ** 31 - 1) if sign == 1 else -2 ** 31
        else:
            return sign * result
