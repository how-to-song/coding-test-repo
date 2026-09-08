class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {}
        magazine_dict = {}

        def insertDict(string, dictionary):
            for ch in string:
                if ch in dictionary:
                    dictionary[ch] += 1
                else:
                    dictionary[ch] = 1

        insertDict(ransomNote, ransomNote_dict)
        insertDict(magazine, magazine_dict)

        for i in ransomNote_dict.keys():
            if i not in magazine_dict or ransomNote_dict[i] > magazine_dict[i]:
                return False
        return True
