import functools as ft

nums = [1, 2, 3]
cube = list(map(lambda i : i * i * i ,nums))
sum = ft.reduce(lambda a,b : a + b , cube)
print (cube)
print(sum)