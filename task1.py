import random

roll_count = 0 
while True:

    num = int(input("How many dice do you want to roll? "))

    print("Rolling dice...")

    for i in range(num):
        dice = random.randint(1, 6)
        print("Dice", i+1, ":", dice)

    roll_count += 1  # increase counter
    print("Total rolls so far:", roll_count)

    # ask to roll again
    again = input("Roll again? (y/n): ")

    if again.lower() != 'y':
        print("Goodbye!")
        break