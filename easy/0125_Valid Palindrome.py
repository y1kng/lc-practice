import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        helper = str.maketrans('', '', string.punctuation)
        s = s.translate(helper)
        s = s.replace(" ", "")
        s = s.lower()
        if s == "":
            return True
        wyk = []
        for i in s:
            wyk.append(i)
        wyk.reverse()
        yk = list(s)
        if yk == wyk:
            return True
        return False




        