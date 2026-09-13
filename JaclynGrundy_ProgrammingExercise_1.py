# Get and validate the number of tickets per user.
def get_tickets(remaining):
    # Ask the amount of tickets the user wants to purchase.
    try:
        tickets = int(input('How many tickets do you need to buy (limit of 4)? '))

        # Check that the user requests between 1 and 4 tickets.
        if tickets < 1 or tickets > 4:
            print('Please enter a ticket amount between 1 and 4.')
            return 0

        # Check that there are enough tickets left to sell to the user.
        if tickets > remaining:
            print('There are not enough tickets left to purchase.')
            return 0

        # Return the valid number of tickets requested.
        return tickets

    # Handles invalid input such as decimals or strings.
    except ValueError:
        print('Please enter a whole number (1, 2, 3 or 4).')
        return 0

# Calculate the remaining tickets and total buyers.
def ticket_sales():
    # Program begins with 20 tickets and 0 buyers.
    remaining = 10
    buyers = 0

    # Continue selling tickets until all have been sold.
    while remaining > 0:
        tickets = get_tickets(remaining)

        # Updates remaining tickets and total buyers.
        if tickets > 0:
            remaining -= tickets
            buyers += 1
            print('Tickets remaining:', remaining)

    # Displays the final results.
    print('No more tickets remaining.')
    print('Total number of buyers:', buyers)

# Execute the ticket_sales function.
ticket_sales()