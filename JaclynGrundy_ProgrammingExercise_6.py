# Imports the regular expression module.
import re

# Validates the format of a phone number.
def validate_phone(phone):
    # Allows 10 digits with optional parentheses, hyphens, periods,
    # or spaces.
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'

    # Returns True if the phone number matches the pattern, otherwise
    # False.
    return bool(re.fullmatch(pattern, phone))

# Validates the format of a Social Security Number.
def validate_ssn(ssn):
    # Requires 3 digits, a hyphen, 2 digits, a hyphen, and 4 digits
    pattern = r'^\d{3}-\d{2}-\d{4}$'

    # Returns True if the SSN matches the pattern, otherwise False.
    return bool(re.fullmatch(pattern, ssn))

# Validates the format of a ZIP code.
def validate_zip(zip_code):
    # Requires 5 digits with no letters or hyphens.
    pattern = r'^\d{5}$'

    # Returns True if the ZIP code matches the pattern, otherwise
    # False.
    return bool(re.fullmatch(pattern, zip_code))

# Tests the validation function with different inputs.
def test_functions():
    print('\nValues used for testing:')
    print('\nTesting phone numbers:')

    # Tests phone numbers with each tuple containing an input and
    # its expected result.
    phone_tests = [('123-456-7890', True), ('(123) 456-7890', True),
                   ('123.456.7890', True), ('1234567890', True),
                   ('123-456-789', False), ('abcdefghij', False)]

    # Runs each phone number test and compares the actual result
    # with the expected result.
    for value, expected in phone_tests:
        result = validate_phone(value)

        # Prints PASS if actual result matches the expected, otherwise
        # prints FAIL.
        print(f"{value}: {'PASS' if result == expected else 'FAIL'}")

    print('\nTesting Social Security Numbers:')

    # Tests SSN examples with each tuple containing an input and
    # its expected result.
    ssn_tests = [('123-45-6789', True), ('123456789', False),
                 ('12-345-6789', False), ('123-456-789', False),
                 ('abc-de-fghi', False)]

    # Runs each SSN test and compares the actual result with the
    # expected result.
    for value, expected in ssn_tests:
        result = validate_ssn(value)

        # Prints PASS if actual result matches the expected, otherwise
        # prints FAIL.
        print(f"{value}: {'PASS' if result == expected else 'FAIL'}")

    print('\nTesting ZIP Codes:')

    # Tests ZIP code examples with each tuple containing an input
    # and its expected result.
    zip_tests = [('12345', True), ('01234', True), ('1234', False),
                 ('123456', False), ('abcde', False)]

    # Runs each ZIP code and compares the actual result with the
    # expected result.
    for value, expected in zip_tests:
        result = validate_zip(value)

        # Prints PASS if the actual result matches the expected,
        # otherwise prints FAIL.
        print(f"{value}: {'PASS' if result == expected else 'FAIL'}")

# Asks the user for input and displays validation results.
def main():
    # Asks the user to enter a phone number, SSN, and ZIP code.
    phone = input('Please enter a phone number (e.g. 123-456-7890): ')
    ssn = input('Please enter a social security number (e.g. 123-45-6789): ')
    zip_code = input('Please enter a ZIP code (e.g. 12345): ')

    print('\nValidation Results:')

    # Checks the phone number and displays whether the format is valid.
    if validate_phone(phone):
        print('Phone number: Valid')
    else:
        print('Phone number: Invalid')

    #Checks the SSN and displays whether the format is valid.
    if validate_ssn(ssn):
        print('Social Security number: Valid')
    else:
        print('Social Security number: Invalid')

    # Checks the ZIP code and displays whether the format is valid.
    if validate_zip(zip_code):
        print('ZIP code: Valid')
    else:
        print('ZIP code: Invalid')

main()
test_functions()