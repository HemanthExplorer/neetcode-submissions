class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        for sr in s:
            if sr in dic1:
                dic1[sr] +=1
            else:
                dic1[sr]=1
        dic2 ={}
        for srt in t:
            if srt in dic2:
                dic2[srt]+=1
            else:
                dic2[srt]= 1
        if dic1 == dic2:
            return True
        else:
            return False
