class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids: 
            a = True
            while stack and stack[-1] > 0 and ast < 0:
                if abs(ast) == stack[-1]:
                    stack.pop()
                    a = False
                    break
                if abs(ast) < stack[-1]:
                    a = False
                    break 
                stack.pop()

            if a:
                stack.append(ast)
            
            
            
            

               
                

        return stack
        