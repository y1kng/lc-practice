from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i, j in enumerate(strs):
            hashmap[i] = sorted(j)
        value_groups = defaultdict(list)
        for k, v in hashmap.items():
            value_groups["".join(v)].append(k)
        res = []
        for value in value_groups.values():
            for u in range(len(value)):
                value[u] = strs[int(value[u])]
            res.append(value)
        return res
        