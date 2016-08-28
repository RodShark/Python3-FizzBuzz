import sys

def main():
    print("Welcome to the FizzBuzz game!")
    print("In this particular game, you set the limit for how high we'll go!")
    print("According to what you typed, we'll be going only up to {}.".format(limit))
    
    for number in range(1, int(limit)+1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz!")
        elif number % 3 == 0:
            print("Fizz!")
        elif number % 5 == 0:
            print("Buzz!")
        else:
            print(number)

if len(sys.argv) <= 1:
    limit = input("Give me a number to set as the highest value we'll be going to. ")
    
    try:
        int(limit)
    except ValueError:
        print("Please give me a numeric number, not a word. :)")
        sys.exit()
        
    main()
    
else:
    limit = sys.argv[1]
    
    try:
        int(limit)
    except ValueError:
        print("Please give me a numeric number, not a word. :)")
        sys.exit()
        
    main()
