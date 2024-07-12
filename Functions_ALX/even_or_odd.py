def identify(num):
    if num % 2 == 0:
        print("{num} is even number")
    else:
        print("{num} is odd number")
    return

num = int(input("Enter a number: "))
identify(num)
