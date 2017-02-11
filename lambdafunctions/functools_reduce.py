from functools import reduce
print(reduce(lambda x,y: x+y, map(lambda x: x**2, range(1,5))))