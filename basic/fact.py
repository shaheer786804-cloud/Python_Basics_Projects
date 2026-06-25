def fact(num):
    res = 1
    for i in range(1 , num+1):
        res = res * i

    return res

num = int(input("Enter a number :"))
result = fact(num)
print(f"factorial of {num} is :" ,result)

