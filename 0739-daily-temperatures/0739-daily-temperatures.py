class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        stack = []
        stack.append((0, temperatures[0]))
        answer = [0 for _ in range(length)]
        
        for i in range(1,length):
            while stack and stack[-1][1] < temperatures[i]:
                idx, temp = stack.pop()
                answer[idx] = i - idx
                
            stack.append((i, temperatures[i]))
                
        return answer
            