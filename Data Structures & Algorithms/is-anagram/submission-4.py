class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            lst = []
            for i in range(len(s)):
                if s[i] not in lst:
                    lst.append(s[i])
            for i in lst:
                if s.count(i) != t.count(i):
                    return False
            return True
                                        





                
                