# Example UI for demonstration purposes
import time

def ui():
    # run loop until user enters valid input(number)
    isValid = False
    while not isValid:
    # get data from user
        data = input("Enter a positive integer and receive a quote: ")
        
    # validate user input
    # write user input to quote-service.txt 
        if data.isnumeric() == True:
            isValid = True
            with open("quote-service.txt", "w") as f:
                # I used a modulo here just for simplicity, however your UI may only allow certain user inputs
                # update modulo value based on number of quotes in database
                data = int(data) % 12
                f.write(str(data))
        else:
            print("Invalid input")
    # wait for quote-service to write quote to text file
    time.sleep(1)
    # read quote from quote-service.txt and display to user
    with open("quote-service.txt", "r") as f:
        quote = f.read()
    print(quote)
    # clear text file
    open("quote-service.txt", "w")

ui()
