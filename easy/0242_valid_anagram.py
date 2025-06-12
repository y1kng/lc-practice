class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w_list = list(t)
        for i in s:
            if i in w_list:           # not t 
                w_list.remove(i)   
            else:
                return False
        if w_list == []:
            return True
        else:
            return False