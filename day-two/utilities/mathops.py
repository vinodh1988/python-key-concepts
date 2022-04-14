from functools import reduce

sum=lambda x,y,z: x+y+z

mul=lambda x:reduce(lambda a,b: a*b,x)