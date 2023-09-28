def gensquares(N):
    for num in range(N):
        yield num**2

for x in gensquares(10):
    print(x)

import random


def rand_num(low,high,n):
    
    for num in range(n):
        yield random.randint(low,high+1)

for num in rand_num(1,10,12):
    print(num)
    

s= 'hello'
i= iter(s)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
