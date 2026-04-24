class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids: 
            destroied = False
            while stack and stack[-1] > 0 and ast < 0:
                if abs(ast) == stack[-1]:
                    stack.pop()
                    destroied = True
                    break
                elif abs(ast) < stack[-1]:
                    destroied = True
                    break 
                stack.pop()
         
            if not destroied:
                stack.append(ast)
                        
        return stack
        