from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        auto_thing = defaultdict(list)

        for i in strs:
            key = ''.join(sorted(i))
            auto_thing[key].append(i)
        
        return list(auto_thing.values())