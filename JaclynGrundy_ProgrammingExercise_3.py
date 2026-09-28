# Import functools to access the reduce function.
import functools

def main():
    # Creates an empty list to store expenses.
    expenses = []

    # Asks the user how many monthly expenses they have.
    while True:
        try:
            num_expenses = int(input('How many monthly expenses do'
                ' you have? '))
            break

        # Handles invalid inputs like strings.
        except ValueError:
            print('Please enter a whole number (1, 2, 3, etc.).')

    # Loops through each expense to get the type and amount.
    for i in range(num_expenses):
        expense_type = input(f'Enter expense #{i + 1} type: ')

        # Keeps asking until a valid number is entered for the
        # expense amount.
        while True:
            try:
                amount = float(input(f'Enter the amount for '
                    f'{expense_type}: $'))
                break

            # Handles invalid inputs like strings.
            except ValueError:
                print('Please enter a numerical amount.')

        # Adds the expense type and amount to the expenses list.
        expenses.append((expense_type, amount))

    # Uses reduce and a lambda function to calculate the total expense.
    total_expense = functools.reduce(lambda total,
        expense: total + expense[1], expenses, 0)

    # Uses reduce and a lambda function to find the highest expense.
    highest_expense = functools.reduce(lambda highest,
        expense: expense if expense[1] > highest[1]
        else highest, expenses)

    # Uses reduce and a lambda function to find the lowest expense.
    lowest_expense = functools.reduce(lambda lowest,
        expense: expense if expense[1] < lowest[1]
        else lowest, expenses)

    # Displays the total monthly amount.
    print(f'Total expense: ${total_expense:.2f}')

    # Checks if all expenses have the same amount.
    if highest_expense[1] == lowest_expense[1]:
        print(f'All expenses are ${highest_expense[1]:.2f}.')
    else:
        # Displays the type and amount of the lowest expense.
        print(f'Highest expense: {highest_expense[0]} - '
          f'${highest_expense[1]:.2f}')

        # Displays the type and amount of the lowest expense.
        print(f'Lowest expense: {lowest_expense[0]} - '
          f'${lowest_expense[1]:.2f}')

# Calls the main function to run the program.
main()