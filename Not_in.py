activity = input("What do you want to do today? ")

if "cinema" not in activity.casefold():     # .casefold() avoids case sensetivity. Means I can write CINEMA
    print("But, I want to go to the cinema")