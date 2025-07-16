class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ik = []
        wyk = ''.join(map(str, digits))
        ly = int(wyk) + 1
        uu = str(ly)
        for i in uu:
            ik.append(int(i))
        return ik