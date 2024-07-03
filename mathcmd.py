import math, random

def add(nums):
    sum = 0
    for x in nums:
        try:
            num = int(x)
        except Exception as e:
            print("NaN Value in arguments.")

        sum = sum + num

    print(sum)
    return True