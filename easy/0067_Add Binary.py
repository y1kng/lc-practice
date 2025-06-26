class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ki = []
        wyk = int(a, 2) + int(b, 2)
        ly = bin(wyk)
        yk = list(ly)
        yk.remove('0')
        yk.remove('b')
        ik = ''.join(yk)
        return ik
