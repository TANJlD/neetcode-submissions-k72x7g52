class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pt = []

        for i in range(len(position)):
            pt.append([position[i], (target-position[i]) / speed[i]])

        pt.sort(key=lambda x:x[0], reverse=True)

        stack = []
        for t in (x[1] for x in pt):                   
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)

        