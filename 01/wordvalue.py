from data import DICTIONARY, LETTER_SCORES

class SignatureDictionary:
    dic = None

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


def init_find_optimal():

    newDictionary = {}
    dictionaryWords = load_words()

    for word in dictionaryWords:
        sign = get_word_signatue(word)

        if newDictionary.has_key(sign):
           newDictionary[sign].append(word)
        else:
            newDictionary[sign] = [word]

    SignatureDictionary.dic = newDictionary

def get_word_signatue(word):
    return ''.join(sorted(word)).upper()

def get_substrings_of_exact_score(i_list, i_score):
    currentList = []
    global_list = []
    get_substrings_of_specific_score_r(global_list, list(i_list), len(i_list), currentList, i_score)
    return set(global_list)

def get_substrings_of_specific_score_r(output_list, i_list, i_listLength, i_subList, i_score):
    if i_score == 0:
        output_list.append(get_word_signatue(i_subList))
        return

    if i_listLength == 0:
        return

    if calc_word_value(i_list[i_listLength - 1]) <= i_score:
        get_substrings_of_specific_score_r(output_list, i_list, i_listLength - 1, i_subList, i_score)
        get_substrings_of_specific_score_r(output_list, i_list, i_listLength - 1, i_subList + [i_list[i_listLength - 1]],
                                           i_score - calc_word_value(i_list[i_listLength - 1]))
    else:
        get_substrings_of_specific_score_r(output_list, i_list, i_listLength - 1, i_subList, i_score)


def find_optimal(i_bunchOfLetters):
    """Find the optimal (highest scoring) word from these letters (including substrings) which is in the dictionary.
    Return it and the score."""

    if SignatureDictionary.dic == None:
        init_find_optimal()

    # Calc the maximum score
    maxPossibleScore = calc_word_value(i_bunchOfLetters)

    # Run from maximum score to 0

    for currentScore in reversed(range(maxPossibleScore + 1)):

        # Find all permutation with this score
        currentScoreWordList = get_substrings_of_exact_score(i_bunchOfLetters, currentScore)

        # For each permutation check if exist in dic
        for word in currentScoreWordList:
            if (SignatureDictionary.dic.has_key(word)):
                identicSignatureWords = SignatureDictionary.dic[word]
                maxWord = identicSignatureWords[0]
                maxWordValue = calc_word_value(maxWord)
                return (maxWord, maxWordValue)

    return (None, 0)


if __name__ == "__main__":
    pass # run unittests to validate
