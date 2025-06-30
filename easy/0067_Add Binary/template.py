class Solution:
    def addBinary(self, a: str, b: str) -> str:
        wyk = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i < 0:
                ol = 0      #String is immutable, use temp variable to hold it
            else:
                ol = int(a[i])         #Safe access with index check                   
            
            if j < 0:      #Same as above
                uu = 0
            else:
                uu = int(b[j])
                                                              # === Initial Incorrect Attempt (for review) ===   
            ly = ol + uu + carry                              #ly = (a[i] + b[j] + carry) % 2
            carry = ly // 2                                   #carry = (a[i] + b[j]) // 2
            wyk.append(str(ly % 2))                           #wyk.append(str(ly))

            i -= 1
            j -= 1

        return ''.join(reversed(wyk))

                