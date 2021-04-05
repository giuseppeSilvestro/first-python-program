# with this program the user will be able to buy tickets for an even

TICKET_PRICE = 10

tickets_remaining = 100

# Output how many tickets are left using the tickets_remaining variable
print('There are {} tickets remaining.'.format(tickets_remaining))


# Gather the user's name and assign it to a new variable
username = input('What is your name? ')

# Prompt the user by name and ask how many tickets they would like
number_of_thickets = int(input('Hello {}! How many tickets would you like? '.format(username)))

# Calculate the price for the total number of thickets
total_price = number_of_thickets * TICKET_PRICE

# Output the price to the screen
print('If you decide to buy the tickets, the total price will be {}'.format(total_price))
