class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c ={}
        t_c ={}
        if len(s) != len(t):
          return False
        for char in s:
            if char in s_c:
                s_c[char]+=1
            else:
                s_c[char]=1
        for char in t:
            if char in t_c:
                t_c[char] +=1
            else:
                t_c[char]= 1
        return s_c == t_c
