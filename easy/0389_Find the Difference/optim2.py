class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = {}
        for v in t:
            hashmap[v] = hashmap.get(v, 0) + 1
        for vv in s:
            hashmap[vv] -= 1
        for i, k in hashmap.items():
            if k == 1:
                return i
         