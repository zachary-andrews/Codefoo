from typing import List
class Temps:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [0 for day in temperatures]
        stack = []
        #for each day
        for i in range(len(temps)):
            temp = temperatures[i]
            while len(stack) and temperatures[stack[-1]] < temp:
                prevIdx = stack.pop()
                temps[prevIdx] = (i - prevIdx)
            stack.append(i)
                    
        return temps
