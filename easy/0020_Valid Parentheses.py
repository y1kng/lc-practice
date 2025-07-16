class Solution:
    def isValid(self, s: str) -> bool:
        ik = []
        for i in s:
            if i in '({[':
                ik.append(i)
        elif i in ')}]':
            if ik and (ik[-1], i) in [('(', ')'), ('[', ']'), ('{', '}')]:
                ik.pop()
        return True if not ik else False