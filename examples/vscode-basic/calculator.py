import numpy as np

def add_numbers(a, b):
    return a + b

def div_num(a,b):
    return a/b

result = add_numbers(5,3)

try:
    result2 = div_num(2,0)
except ZeroDivisionError as e:
    print(f"Error: {e}")

print(f"The result is: {result}")

for i in range(20):
    print(i)
    print(div_num(3,i))


