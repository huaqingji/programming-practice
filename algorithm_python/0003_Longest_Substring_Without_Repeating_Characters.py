from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        counter = defaultdict(int) # a counter for the window
        left, ans = 0, 0

        for right in range(len(s)):
            char = s[right]
            counter[char] += 1
            while counter[char] > 1:
                counter[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
        