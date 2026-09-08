class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_val_key = {}
        dict_key_val = {}

        s_list = s.split()

        if len(pattern) != len(s_list):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in dict_key_val:
                dict_key_val[pattern[i]] = s_list[i]
            else:
                if dict_key_val[pattern[i]] != s_list[i]:
                    return False
            
            if s_list[i] not in dict_val_key:
                dict_val_key[s_list[i]] = pattern[i]
            else:
                if dict_val_key[s_list[i]] != pattern[i]:
                    return False

        return True