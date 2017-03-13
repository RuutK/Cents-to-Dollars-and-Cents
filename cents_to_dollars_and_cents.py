# This simple program shows the correct way to display dollars and cents (to avoid "1 dollars" or "1 cents" situations.)

total_amount_of_cents = int(input("Insert the total amount of cents: "))

amount_of_dollars = total_amount_of_cents // 100
remaining_cents = total_amount_of_cents % 100

# 1 cent
if amount_of_dollars == 0 and remaining_cents == 1:
    print("This is " + str(remaining_cents) + " cent.")

# 0 or 2 to 99 cents
if amount_of_dollars == 0 and remaining_cents != 1:
    print("This is " + str(remaining_cents) + " cents.")

# 1 dollar
if amount_of_dollars == 1 and remaining_cents == 0:
    print("This is " + str(amount_of_dollars) + " dollar.")

# 1 dollar and 1 cent
if amount_of_dollars == 1 and remaining_cents == 1:
    print("This is " + str(amount_of_dollars) + " dollar and " + str(remaining_cents) + " cent.")

# 1 dollar and 2 to 99 cents
if amount_of_dollars == 1 and remaining_cents > 1:
    print("This is " + str(amount_of_dollars) + " dollar and " + str(remaining_cents) + " cents.")

# 2 to endless amount of dollars without cents
if amount_of_dollars > 1 and remaining_cents == 0:
    print("This is " + str(amount_of_dollars) + " dollars.")

# 2 to endless amount of dollars and 1 cent
if amount_of_dollars > 1 and remaining_cents == 1:
    print("This is " + str(amount_of_dollars) + " dollars and " + str(remaining_cents) + " cent.")

# 2 to endless amount of dollars and 2 to 99 cents
if amount_of_dollars > 1 and remaining_cents > 1:
    print("This is " + str(amount_of_dollars) + " dollars and " + str(remaining_cents) + " cents.")