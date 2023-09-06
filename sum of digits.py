sumOfDigits = 0
num = int(input("Enter the number:"))
while(num!=0):
    temp = num % 10
    sumOfDigits = sumOfDigits + temp
    num = num // 10

print("The sum of digits is :",sumOfDigits)
