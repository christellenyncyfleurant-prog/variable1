num1 = int(input("Enter the first number for multiplication"))
num2 = int(input("Enter the second number for multiplication"))
dividend = int(input("Enter the dividend"))
divisor = int(input("Enter the divisor"))
num3 = int(input("Enter number for addition"))
num4 = int(input("Enter second number for addition"))
num5 = int(input("Enter number for substraction"))
num6 = int(input("Enter second number for substraction"))

#Multiplication
question1 = num1 * num2
print("The answer to your query is", question1)
#Division
question2 = dividend / divisor
print("The answer to your query is", question2)
#Division without remainder
question3 = dividend // divisor
print("The answer to your query is", question3)
#Remainder only
question4 = dividend % divisor
print("The answer to your query is", question4)
#Addition
question5 = num3 + num4
print("The answer to your query is", question5)
#Substraction
question6 = num5 - num6
print("The answer to your query is", question6)

# Print your name at the end of the program
name = input("Enter your name: ")
print("My name is",name)
