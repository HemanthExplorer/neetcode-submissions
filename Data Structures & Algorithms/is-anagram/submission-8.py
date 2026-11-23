class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        c_s,c_t = {},{}

        for i in s:
            if i in c_s:
                c_s[i]+=1
            else:
                c_s[i]= 1
            
        for j in t:
            if j in c_t:
                c_t[j]+=1
            else:
                c_t[j]= 1

        return c_s ==c_t   