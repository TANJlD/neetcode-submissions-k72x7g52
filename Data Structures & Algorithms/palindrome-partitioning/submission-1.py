class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(s):
            l = 0
            r = len(s) - 1
            while s[l] == s[r] and l < r:
                l += 1
                r -= 1
            return not l < r

        n = len(s)
        row = [False] * n
        Map = [row.copy() for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                if isPal(s[i:j+1]):
                    Map[i][j] = True

        result = []
        curr = []
        def check(l):
            if l == n:
                result.append(curr.copy())
                return

            for i in range(l, n):
                if Map[l][i]:
                    curr.append(s[l: i+1])
                    check(i+1)
                    curr.pop()

        check(0)
        return result

                
