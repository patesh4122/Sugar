while True:
    try:
        first_number = int(input("What is the first number you want to add?"))
        secound_number = int(input("What is the second number you want to add?"))
        sum = first_number + secound_number
        print("The sum of your two number is", sum)
        break
    except:
        print("You are dumb. That is not an integer...")
