class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        point1 = 0
        point2 = 0
        stack = []

        while point1 < len(pushed) and point2 < len(popped):
            if pushed[point1] == popped[point2]:
                point1 += 1
                point2 += 1
            elif stack and popped[point2] == stack[-1]:
                stack.pop()
                point2 += 1
            else:
                stack.append(pushed[point1])
                point1 += 1
                
        while point2 < len(popped):
            if stack[-1] != popped[point2]:
                return False
            
            point2 += 1
            stack.pop()

        return True
        