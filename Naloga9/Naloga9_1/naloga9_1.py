

print("Hello User, I can convert kilometres you enter into miles!  ")

user_input = None


while True:

    user_input =  int (input("Please enter kilometres you want to convert: " ))
    miles = user_input * 0.621371192
    print("Your " + str(user_input) + " KM is same as " + str(miles) +" miles")
    
    end = input( "Do you want to end the game? (y/n)? " )

    if end == "y":
        break