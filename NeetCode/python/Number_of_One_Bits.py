class Solution:
    def hammingWeight(self, n: int) -> int:
        count_ones=0
        while n>0:
            count_ones+=n%2
            n=n//2

        return count_ones
