class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pt = []

        for i in range(len(position)):
            pt.append([position[i], (target-position[i]) / speed[i]])

        pt.sort(key=lambda x:x[0], reverse=True)

        stack = []
        fleet = 0
        for t in (x[1] for x in pt):                   
            while stack and t > stack[-1]:
                stack.pop()
                if not stack:
                    fleet += 1
            stack.append(t)

        if stack and stack[0] >= stack[-1]:
            return fleet + 1

        return fleet + len(stack)




        

        