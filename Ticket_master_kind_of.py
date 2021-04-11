# with this program the user will be able to buy tickets for an even

TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

# Calculate the final price including a service charge for each transaction
def calculate_price(number_of_tickets):
    return number_of_tickets * TICKET_PRICE + SERVICE_CHARGE

# Run this code till there are no tickets left
while tickets_remaining > 1:
    # Output how many tickets are left using the tickets_remaining variable
    print('There are {} tickets remaining.'.format(tickets_remaining))


    # Gather the user's name and assign it to a new variable
    username = input('What is your name? ')


    # handle possible exception
    try:
        # Prompt the user by name and ask how many tickets they would like
        number_of_tickets = int(input('Hello {}! How many tickets would you like? '.format(username)))
        # print an error message if the number of tickets requested are more than#
        #the tickets available
        if number_of_tickets > tickets_remaining:
            raise ValueError('There are only {} tickets remaining'.format(tickets_remaining))
    except ValueError as err:
        print('You did not input a valid value. {} Please try again'.format(err))
    else:
        # Calculate the price for the total number of thickets
        total_price = calculate_price(number_of_tickets)

        # Output the price to the screen
        print('If you decide to buy the tickets, the total price will be {}'.format(total_price))

        # Prompt user if the want to proceed
        user_choice = input('{} would you like to proceed with your order? Y/N '.format(username))
        # If the want to proceed
        if user_choice.lower() == 'y':
            # print out to the screen "SOLD!"
            print('SOLD!')
            # reduce the tickets remaining
            tickets_remaining -= number_of_tickets
        # Otherwise
        else:
            print('Your order has not been processed.')

        # thank them by name
        print('Thank you for stopping by, {}'.format(username))

# notify the user that the tickets are sold out
print('There are no tickets left!')
