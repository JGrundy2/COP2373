# Imports the regular expression module.
import re

# Function to split the paragraph into sentences.
def split_sentences(paragraph):
    # Regular expression for sentences beginning with a letter or number
    # and ending with a period, exclamation mark, or question mark.
    # Allows multiple spaces between sentences.
    pattern = r'[a-z0-9].*?(?<!\d)[.!?](?=\s*[a-z0-9]|$)'

    # Finds all sentences using the pattern and allows uppercase and
    # lowercase letters to match.
    matches = re.finditer(pattern, paragraph, re.IGNORECASE)

    # Takes each sentence and removes any extra spaces from its ends.
    # The original capitalization and punctuation are still present.
    sentences = [match.group().strip() for match in matches]

    # Return the list of sentences to the calling function.
    return sentences

# Function to count how many sentences are in the paragraph.
def count_sentences(sentences):
    # Returns the number of sentences in the list.
    return len(sentences)

# Function to ask the user for a paragraph and displays the results.
def main():
    try:
        # Asks the user to enter a paragraph.
        paragraph = input('Please enter a paragraph: ')

        # Checks to see if the paragraph contains only spaces.
        if not paragraph.strip():
            raise ValueError('The paragraph must not be empty. Try again.')

        # Checks to see if the paragraph ends with a period, exclamation mark,
        # or question mark. Ignores any spaces that may be at the end.
        if not paragraph.rstrip().endswith(('.', '!', '?')):
            raise ValueError('The paragraph must end with a period, '
                             'exclamation mark, or question mark. '
                             'Try again.')

        # Splits the paragraph into sentences.
        sentences = split_sentences(paragraph)

        # checks to see if the regular expression found any valid sentences.
        if not sentences:
            raise ValueError('No valid sentences were found. Try again.')

        # Displays each sentence.
        print('\nIndividual sentences:')

        # Numbers each sentence by starting with 1.
        for number, sentence in enumerate(sentences, start=1):
            print(f'{number}. {sentence.strip()}')

        # Counts and displays the total number of sentences in the
        # paragraph.
        print('\nTotal number of sentences:', count_sentences(sentences))

    # Catches ValueError exceptions and displays the corresponding error
    # message.
    except ValueError as error:
        print('Error:', error)

main()

