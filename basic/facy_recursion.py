def fact(num):

    if num == 1:
        return 1

    return num * fact(num - 1)

number = int(input("Enter a Number :"))
result = fact(number)
print (f"Factor of {number} is :" ,result)

