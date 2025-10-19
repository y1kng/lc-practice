from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        auto_thing = defaultdict(list)
        for i, j in enumerate(s):
            auto_thing[j].append(t[i])
        for g, v in auto_thing.items():
            if len(set(v)) != 1:
                return False
            else:
                auto_thing[g] = list(set(v))
        new_hash = {}
        for p, k in auto_thing.items():
            new_hash[''.join(k)] = p
        if len(new_hash) == len(auto_thing):
            return True
        else:
            return False
