class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        characters_s = list(s)
        characters_t = list(t)
        s_dict = {}
        t_dict = {}

        for c_s in characters_s:
            if c_s not in s_dict.keys():
                s_dict[c_s] = 1
            else:
                s_dict[c_s] += 1

        for c_t in characters_t:
            if c_t not in t_dict.keys():
                t_dict[c_t] = 1
            else:
                t_dict[c_t] += 1 

        for key in s_dict.keys():
            if key not in t_dict.keys():
                return False
            else:
                if s_dict[key] != t_dict[key]:
                    return False
                else:
                    del t_dict[key]

        return len(t_dict) == 0                                  

        