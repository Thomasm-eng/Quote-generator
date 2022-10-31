# read command from text file and provide quote

def quoteService():
    # declare list of quotes
    # I pulled an example list of quotes from: https://www.shopify.com/blog/motivational-quotes
    quoteList = ["Success is not final; failure is not fatal: It is the courage to continue that counts. — Winston S. Churchill",
    "It is better to fail in originality than to succeed in imitation. — Herman Melville",
    "The road to success and the road to failure are almost exactly the same. — Colin R. Davis",
    "Success usually comes to those who are too busy looking for it. — Henry David Thoreau",
    "Develop success from failures. Discouragement and failure are two of the surest stepping stones to success. —Dale Carnegie",
    "Nothing in the world can take the place of Persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb. Education will not; the world is full of educated derelicts. The slogan 'Press On' has solved and always will solve the problems of the human race. —Calvin Coolidge",
    "There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind. —Mister Rogers",
    "Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable. —John Wooden",
    "Setting goals is the first step in turning the invisible into the visible. — Tony Robbins",
    "Success is getting what you want, happiness is wanting what you get. ―W. P. Kinsella",
    "Concentrate all your thoughts upon the work in hand. The sun's rays do not burn until brought to a focus.  — Alexander Graham Bell",
    "Either you run the day or the day runs you. — Jim Rohn",
    "I'm a greater believer in luck, and I find the harder I work the more I have of it. — Thomas Jefferson"]
    
    # read number from quote-service.txt
    isRead = False
    while not isRead:
        with open("quote-service.txt", "r") as f:
            data = f.read()
        # check that data is not an empty string(text file is empty)
        if data != "":
            isRead = True
    # write quote at selected index to quote-service.txt
    with open("quote-service.txt", "w") as f:
        f.write(quoteList[int(data)])

quoteService()
