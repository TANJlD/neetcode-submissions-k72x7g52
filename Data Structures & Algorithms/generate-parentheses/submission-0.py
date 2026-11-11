class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        pars = []
        result = []


        def generate(open, close):
            if len(pars) == n * 2:
                result.append("".join(pars))
                return

            if open < n:
                pars.append("(")
                open += 1
                generate(open, close)
                pars.pop()
                open -= 1

            if close < open:
                pars.append(")")
                close += 1
                generate(open, close)
                pars.pop()
                close -= 1


        generate(0, 0)
        return result
        