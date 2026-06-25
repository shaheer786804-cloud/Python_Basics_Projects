def add(num1 , *num2):
    sum = num1
    for n in num2:
        sum += n

    return sum

result = add(4,6,3,7,4,2,6,7)    
print(result)
