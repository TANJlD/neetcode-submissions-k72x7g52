class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        curr = []
        n = len(s)

        def isPal(st):
            l, r = 0, len(st) - 1
            while l < r:
                if not st[l].isalnum():
                    l += 1
                elif not st[r].isalnum():
                    r -= 1
                else:
                    if st[l].lower() != st[r].lower():
                        return False
                    l += 1
                    r -= 1
            return True


        def check(l):
            if curr and not isPal(curr[-1]):
                return 
            if l == n:
                result.append(curr.copy())
                return    

            for i in range(l, n):
                curr.append(s[l:i+1])
                check(i+1)
                curr.pop()

        check(0)
        return result
        