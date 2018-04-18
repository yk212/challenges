from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""

    with open(DICTIONARY) as dictionaryFile:
        dictionaryLines = dictionaryFile.readlines()

    dictionaryWords = [line.rstrip() for line in dictionaryLines]

    return dictionaryWords

def calc_word_value(i_word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    wordValue = 0
    for letter in i_word.upper():
        if LETTER_SCORES.has_key(letter):
            wordValue += LETTER_SCORES[letter]

    return wordValue

def max_word_value(i_words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    maxWord = max(i_words, key=calc_word_value)
    return maxWord

def find_optimal(i_bunchOfLetters):


    pass # Tuple[str,int]:

if __name__ == "__main__":
    pass # run unittests to validate
