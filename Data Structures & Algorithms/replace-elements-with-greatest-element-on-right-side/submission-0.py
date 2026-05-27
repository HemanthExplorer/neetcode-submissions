class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_r = -1
        for i in range(len(arr))[::-1]:
            prev_m = max_r
            max_r = max(arr[i], max_r)
            arr[i] = prev_m
        arr[-1] = -1
        return arr