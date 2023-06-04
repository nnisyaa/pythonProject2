number = int(input("Choose a number from 1-100"))
if number > 100 or number < 1:
    print("error")
elif number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")


salary = 200
num1 = 200
num2 = 200
per = 0.3

per1 = int(input("sales of manager1"))
per2 = int(input("sales of manager2"))
per3 = int(input("sales of manager3"))

if per1 <= 