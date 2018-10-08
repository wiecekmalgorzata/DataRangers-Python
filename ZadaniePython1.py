# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# wykorzystana funkcja sum()
def avg(input):
    return sum(input)/len(input)

print(avg([2,2,2,2,2,2]) - 2 < 0.0000001)
print(avg([4, 6, 55, 18, 17, 12]) - 18.666666666666668 < 0.0000001)
print(avg([86, 89, 24, 45, 62, 17, 61, 63, 30, 13]) - 49 < 0.0000001)

# pętlą
def avg1(input):
    c=0
    for i in range(len(input)):
        c+=input[i]
    return c/len(input)

print(avg1([1,7,1]))
print(avg1([2,2,2,2,2,2]) - 2 < 0.0000001)
print(avg1([4, 6, 55, 18, 17, 12]) - 18.666666666666668 < 0.0000001)
print(avg1([86, 89, 24, 45, 62, 17, 61, 63, 30, 13]) - 49 < 0.0000001)