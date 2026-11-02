# Imports the csv module.
import csv

# Collects student information and writes it to a CSV file.
def write_grades():
    # Asks the user how many students they want to enter.
    try:
        num_students = int(input('How many students would you like to '
                                 'enter? '))

        # Makes sure the number of students is greater than 0.
        if num_students <=0:
            print('Please enter a number greater than 0.')
            return

    # Displays an error if the number of students entered is a decimal.
    except ValueError:
        print('Please enter a whole number of students.')
        return

    # Opens the CSV file in write mode and creates it if it does not
    # exist already.
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Writes the column headings in the CSV file.
        writer.writerow(['First name', 'Last name', 'Exam 1', 'Exam 2',
                         'Exam 3'])

        # Loops through each student based on the number entered.
        for student in range(num_students):
            print('\nPlease enter information for student', student + 1)

            # Asks for the student's name.
            first_name = input('First Name: ')
            last_name = input('Last Name: ')

            # Creates an empty list to store the student's exam grades.
            grades = []

            # Loops through the three exams.
            for exam in range(1, 4):
                while True:
                    try:
                        # Asks the exam grade and converts the input to
                        # a float.
                        grade = float(input('Exam ' + str(exam) +
                                            ' grade: '))
                        # Adds the exam grade to the grades list.
                        grades.append(grade)
                        break
                    # Displays an error if the grade includes a percent
                    # sign.
                    except ValueError:
                        print('Please enter a number without a percent '
                              'sign.')

            # Writes the student's name and exam grades as a CSV record.
            writer.writerow([first_name, last_name] + grades)

    # Lets the user know the grades have been saved.
    print('\nGrades have been saved to grades.csv.')

# Reads the CSV file and displays the student grades in a table.
def read_grades():
    # Opens the CSV file in read mode.
    with open('grades.csv', 'r', newline='') as file:
        reader = csv.reader(file)

        # Reads the column headings.
        header = next(reader)

        # Displays the headings in a table.
        print('\n{:<15} {:<15} {:<10} {:<10} {:<10}'.format(header[0],
                header[1], header[2], header[3], header[4]))

        # Loops through each remaining row in the CSV file.
        for row in reader:
            # Displays each student's information in columns.
            print('{:<15} {:<15} {:<10} {:<10} {:<10}'.format(row[0],
                    row[1], row[2], row[3], row[4]))


write_grades()
read_grades()