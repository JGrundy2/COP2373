# Sets up the list of spam terms that will be checked for in the email.
def get_spam_terms():
    spam_terms = ['act now', 'urgent', 'immediately', 'you must act',
                  'verify your account', '100% free', 'legal notice',
                  'final warning', 'lawsuit', 'legal action',
                  'action required', 'antivirus', 'data breach',
                  'password reset', 'security breach', 'malware detected',
                  'free download', 'no cost', 'last chance', 'limited time',
                  'incredible deal', 'serious cash', 'credit card',
                  'get rich', 'earn money', 'order now', 'today only',
                  'offer expires', 'save big', 'jackpot']

    # Returns the list of spam terms.
    return spam_terms

# Keeps track of spam terms found and how often it occurs.
def check_spam(email, spam_terms):
    # Initialize the spam score to 0.
    score = 0

    # Creates a list to hold the spam terms found in the email.
    found_terms = []

    # Converts email to lowercase letters so all versions of the spam term
    # will be detected.
    email = email.lower()

    # Checks for spam terms in the email.
    for word in spam_terms:
        # Counts how many times a term appears in the email.
        count = email.count(word)

        # Adds number of times a term appears to the spam score.
        if count > 0:
            score += count
            # Adds what spam terms were used to the found_terms list.
            found_terms.append(word)

    # Returns the spam score and the specific spam terms found.
    return score, found_terms

# Gets email and displays spam score and terms.
def main():
    # Gets the list of spam terms.
    spam_terms = get_spam_terms()

    # Asks the user to write an email.
    email = input('Enter the email you wish to send: ')

    # Checks the email to get the spam terms and the total score.
    score, found_terms = check_spam(email, spam_terms)

    # Display the spam score.
    print('spam score:', score)

    # Displays chance of spam depending on total spam score.
    if score == 0:
        print('Possibility of spam: very unlikely')
    elif score <= 5:
        print('Possibility of spam: reasonable chance')
    else:
        print('Possibility of spam: very likely')

    # Displays the specific spam terms found.
    print('Spam terms found:')

    # Goes through each spam term that was found and displays them.
    for word in found_terms:
        print('-', word)

# Calls the main function to run the program.
main()