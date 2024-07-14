import math, random

configs = {
    'angle':'deg',
    'acc':4
}

def mathing():
    print("Begin mathing.")
    arguments = []
    command = None
    mathcmds = {
        "add":"add({0})",
        "exit":"return None",
        "trig":"trig()",
        "config":"config({0},{1})"
    }
    while True:
        if command == "exit":
            break
        command = input("chat>math>").lower()
        parts = command.split()
        command = parts[0]
        arguments = parts[1:]
        try:
            exec(mathcmds[command].format(arguments))
        except Exception as e:
            if not mathcmds.__contains__(command):
                print("Invalid Math Command.")




def add(nums):
    sum = 0
    for x in nums:
        num = parse_num(x)
        if num == "invalid_number":
            print("NaN Value in arguments.")
            return None

        sum = sum + num

    print(sum)
    return True

def parse_num(num):
    consts = {
        'e':math.e,
        'pi':math.pi,
        'g':9.8,
        'phi':(1 + 5 ** 0.5) / 2 #golden ratio
    }
    try:
        num = int(num)
        return num
    except Exception as e:
        if consts.__contains__(num):
            return consts[num]
        
        else:
            print(num[0])
            if num[0:2] == 'r.':
                root = math.sqrt(parse_num(num[2:]))
                return root
            
        return "invalid_number"

def config(attr, val):
    print(attr, val)
    if attr == 'angle':
        if ['deg','rad'].__contains__(val):
            print(True)
            configs['angle'] = val
            print(f"{attr} replaced with {val}")
        else:
            print("Invalid input, expected deg or rad.")
            return None
    elif attr == 'acc':
        try:
            val = int(val)
        except:
            print("Expected whole number value.")
            return
        if val < 10:
            configs['acc'] = val
            print(f"{attr} replaced with {val}")
        else:
            print("Number too large, expected less than 10.")
            return
        
