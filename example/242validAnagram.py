class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        vocabulary = {}
        for i in range(len(s)):
            vocabulary[s[i]] = vocabulary.get(s[i], 0) + 1
            vocabulary[t[i]] = vocabulary.get(t[i], 0) - 1

        for key, value in vocabulary.items():
            if value != 0:
                return False

        return True
    
    
a = Solution()
print(a.isAnagram("anagram",
"nagaram"))

a = 'aslfhqoi'
print(list(a))