class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # If str2 is longer than str1, it's impossible for it to be a subsequence
        if len(str2) > len(str1):
            return False

        # Initialize pointers for str1 and str2
        i, j = 0, 0

        # Traverse both strings
        while i < len(str1) and j < len(str2):
            # Check if str1[i] matches str2[j] directly or after incrementing cyclically
            if str1[i] == str2[j] or (chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]):
                # Move the pointer in str2
                j += 1
            # Always move the pointer in str1
            i += 1

        # If we have matched all characters in str2, return True
        return j == len(str2)

        