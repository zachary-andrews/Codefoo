import re
class decode:
    
    def add_words(self, code: str) -> str:
        resultstr = ""
        holder = ""
        numbys = list(filter(None,code.split("]")))
        for numby in numbys:
            if numby[0].isalpha():
                holder = numby[0]
                numby = numby[1:]
            if len(numby.split("[")) < 2:
                string = numby
                numb = 1
            else:
                numb,string=numby.split("[")
            resultstr += holder+int(numb)*string
        return resultstr

    def check_nested(self, code: str) -> str:
        open = False
        for c in code:
            if c == '[' and open:
                return True
            elif c == '[' and not open:
                open = True
            elif c == ']' and open:
                open = False
        return False
             
    def handle_nested(self,code: str) -> str:
        adderstring = self.add_words(code[code.find("[")+1:code.rfind("]")])
        return code.replace(code[code.find("[")+1:code.rfind("]")],adderstring)
        
    def get_word(self, code):
        if self.check_nested(code):
            opens = code.count('[')
            for i in range(opens):
                code = self.handle_nested(code)
            return self.add_words(code)

        else:
            return self.add_words(code)

