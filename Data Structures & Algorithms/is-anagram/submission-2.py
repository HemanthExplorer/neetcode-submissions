class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        for sr in s:
           dic1[sr] = dic1.get(sr,0)+1
        dic2 ={}
        for srt in t:
            if srt in dic2:
                dic2[srt]+=1
            else:
                dic2[srt]= 1
        return dic1 == dic2
            