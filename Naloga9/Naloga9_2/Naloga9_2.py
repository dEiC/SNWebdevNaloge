#FizzBuzz program

# User enters a number between 1 and 100
# FizzBuzz program starts to count to that number (it prints them in the Terminal). In case the number is divisible with 3, it prints "fizz" instead of the number. 
# If the number is divisible with 5, it prints "buzz". If it's divisible with both 3 and 5, it prints "fizzbuzz".



number1 = 1
user_number = None

print("Hello User, We will do some FizBuzzing")
user_number = int(input("Please enter a random number between 1 and 100: "))

while number1 <= user_number:
    #print(number1)
    #number1 += 1

    
    if number1 % 3 == 0 and  number1 % 5 == 0:
        print("FizzBuzz")

    elif number1 % 5 == 0:
        print("Buzz")

    elif number1 % 3 == 0:
        print("Fizz")

    else:
        print(number1)
    number1 += 1    
