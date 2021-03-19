class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for op in ops:
            try:
                scores.append(int(op))
            except:
                if op == 'C':
                    scores.pop()    

                elif op == 'D':
                    new_val = scores[-1]*2
                    scores.append(new_val)

                elif op == '+':
                    val_sum = scores[-2] + scores[-1]
                    scores.append(val_sum)

                else:
                    print("invalid op") 
                
        print(scores)   
        return sum(scores)