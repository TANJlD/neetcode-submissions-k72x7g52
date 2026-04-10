class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1

        while i < j:
            while not (s[i].isalpha() or s[i].isdigit()):
                i += 1
                if i == (len(s) - 1):
                    return True
            while not (s[j].isalpha() or s[j].isdigit()):
                j -= 1
                if j == 0:
                    return True
            
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True


        