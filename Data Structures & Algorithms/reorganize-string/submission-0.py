from math import ceil 

class Solution:
    def reorganizeString(self, s: str) -> str:
        letters = defaultdict(int)
        ans = ["."] * len(s)
        most_freq = 0
        most_freq_l = ""
        stack = []

        for l in s:
            letters[l] += 1
            if letters[l] > ceil(len(s)/2):
                return ""
            if letters[l] > most_freq:
                most_freq = letters[l]
                most_freq_l = l

        del letters[most_freq_l]

        for k, v in letters.items():
            stack.append([k] * v)

        stack.append([most_freq_l] * most_freq)

        print(stack)

        for i in range(len(s)):
            if i % 2 == 0:
                ans[i] = stack[-1].pop()
                if not stack[-1]:
                    stack.pop()

        for i in range(len(s)):
            if i % 2 !=  0:
                ans[i] = stack[-1].pop()
                if not stack[-1]:
                    stack.pop()

        return "".join(ans)

        