import cmath as math
import random #future use ig
from base import Base

class Math(Base):
    configs = {
        'angle':'deg',
        'acc':4
    }
    
    def __init__(self) -> None:
        super().__init__("math")
        mathcmds = {
            "add":"self.add({0})",
            "multi":"self.multi({0})",
            "config":"self.config({0})"
        }
        mathhelp = {
            "add":"Add numbers together",
            "multi":"Multiply numbers together",
            "config":"Modify Module configuration."
        }
        mathusage = {
            "add":"add [a] [b] [c] .....",
            "multi":"multi [a] [b] [c] .....",
            "config":"config [attr] [val]"
        }
        self.cmds.update(mathcmds)
        self.helps.update(mathhelp)
        self.usage.update(mathusage)

    def add(self, nums):
        sum = 0
        for x in nums:
            num = self.parse_num(x)
            if num == "invalid_number":
                print("NaN Value in arguments.")
                return None

            sum = sum + num
        sum=round(sum,self.configs["acc"])
        print(sum)
        return True

    def multi(self, nums):
        product = 1
        for x in nums:
            num = self.parse_num(x)
            if num == "invalid_number":
                print("NaN Value in arguments.")
                return None

            product = product * num
        product=round(product,self.configs["acc"])
        print(product)
        return True

    def parse_num(self, num):
        consts = {
            'e':math.e,
            'pi':math.pi,
            'g':9.8,
            'phi':(1 + 5 ** 0.5) / 2 #golden ratio
        }
        try:
            num = float(num)
            return num
        except Exception as e:
            if consts.__contains__(num):
                return consts[num]
            else:
                if num[0:2] == 'r.':
                    root = math.sqrt(self.parse_num(num[2:]))
                    return root
                
            return "invalid_number"

    def config(self,attr, val):
        print(attr, val)
        if attr == 'angle':
            if ['deg','rad'].__contains__(val):
                print(True)
                self.configs['angle'] = val
                print(f"{attr} replaced with {val}")
            else:
                print("Invalid input, expected deg or rad.")
                return None
        elif attr == 'acc':
            try:
                val = int(val)
            except:
                print("Expected whole number value less than 10.")
                return
            if 0 < val < 10:
                configs['acc'] = val
                print(f"{attr} replaced with {val}")
            else:
                print("Number too large, expected less than 10.")
                return
        else:
            print("Invalid attribute.")
            return
