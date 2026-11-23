# Imports the numpy module.
import numpy as np

# Function that loads the student grades from the grades.csv file.
def load_grades():
    # Skips the header and student name columns in the file.
    grades = np.genfromtxt('grades.csv', delimiter=',',
    skip_header=1, usecols=(2, 3, 4))

    return grades

# Function that calculates the statistics for each exam.
def exam_stats(grades):
    print('\nStatistics for each exam:')

    # Loops through each exam and performs the calculations with rounding
    # for the mean, median, and standard deviation.
    for exam in range(3):
        exam_grades = grades[:, exam]

        print('\nExam', exam + 1)
        print('Mean:', round(np.mean(exam_grades), 2))
        print('Median:', round(np.median(exam_grades), 2))
        print('Standard Deviation:', round(np.std(exam_grades), 2))
        print('Minimum:', np.min(exam_grades))
        print('Maximum:', np.max(exam_grades))

# Function that calculates the statistics for all exams together.
def overall_stats(grades):
    # Combines all exam grades into one array.
    all_grades = grades.flatten()

    # Performs calculations for all exams with rounding for the mean,
    # median, and standard deviation.
    print('\nOverall statistics:')
    print('Mean:', round(np.mean(all_grades), 2))
    print('Median:', round(np.median(all_grades), 2))
    print('Standard Deviation:', round(np.std(all_grades), 2))
    print('Minimum:', np.min(all_grades))
    print('Maximum:', np.max(all_grades))

# Function that counts the passing and failing grades for each exam.
def pass_fail_amount(grades):
    print('\nThe number of passes and fails for each exam:')

    # Loops through each exam.
    for exam in range(3):
        exam_grades = grades[:, exam]

        # Considers grades of 60 or higher as passing and anything
        # below that failing.
        passed = np.sum(exam_grades >= 60)
        failed = np.sum(exam_grades < 60)

        # Displays the number of students who passed and failed
        # each exam.
        print('\nExam', exam + 1)
        print('Number of passes:', passed)
        print('Number of fails:', failed)

# Function that calculates the total pass rate for all exams.
def overall_pass_percentage(grades):
    # Counts all passing grades.
    passed = np.sum(grades >= 60)

    # Gets the total number of grades.
    total_grades = grades.size

    # Calculates the passing percentage.
    percentage = (passed / total_grades) * 100

    # Displays the total pass rate rounded to the second decimal
    # point.
    print('\nOverall pass percentage:')
    print(f'{percentage:.2f}%')

# Function that loads and displays grades from the grades.csv file
# and calls other functions.
def main():
    # Loads the grades from the grades.csv file.
    grades = load_grades()

    # Displays the first five rows of exam grades from the file.
    print('First few rows of student grades:')
    print(grades[:5])

    # Calls the other functions to calculate the statistics.
    exam_stats(grades)
    overall_stats(grades)
    pass_fail_amount(grades)
    overall_pass_percentage(grades)

main()
