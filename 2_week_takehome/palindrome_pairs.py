class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        def is_palindrome(check):
            return check == check[::-1]

        words_to_index = {w: i for i, w in enumerate(words)}
        palindrome_pairs = set()  # Using a set to avoid duplicates

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]

                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back in words_to_index and words_to_index[back] != i:
                        palindrome_pairs.add((words_to_index[back], i))

                if j > 0 and is_palindrome(suffix):
                    front = prefix[::-1]
                    if front in words_to_index and words_to_index[front] != i:
                        palindrome_pairs.add((i, words_to_index[front]))

        # Handle special case for empty string
        if "" in words:
            empty_index = words_to_index[""]
            for i, word in enumerate(words):
                if i != empty_index and is_palindrome(word):
                    palindrome_pairs.add((i, empty_index))
                    palindrome_pairs.add((empty_index, i))

        return list(palindrome_pairs)
