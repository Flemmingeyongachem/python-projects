from functools import reduce
numbers=[3,5,6,13,2,4,97,6,5,12]
num=[34,6,4,8,9,0,12,34,56,78]
evens=list(filter(lambda n:n%2==0,numbers))
doubles=list(map(lambda n:n*2,evens))
print(doubles)
sun=reduce(lambda a,b:a+b,doubles)
print(sun)
#filter,zip,map,dict comprehension,
# print(evens)