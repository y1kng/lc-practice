class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 11:
            return []
        hashmap = {}
        i = 0
        j = 9
        while j < len(s):
            hashmap[s[i:j + 1]] = hashmap.get(s[i:j + 1], 0) + 1
            j += 1
            i += 1
        res = []
        for k, v in hashmap.items():
            if v > 1:
                res.append(k)
        return res
