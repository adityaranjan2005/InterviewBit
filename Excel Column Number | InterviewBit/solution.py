class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        result = 0
        for char in A:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result
