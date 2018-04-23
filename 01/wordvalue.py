from data import DICTIONARY, LETTER_SCORES


class SignatureDictionary:
    dic = None


def load_words():
    """Load dictionary into a list and return list"""

    with open(DICTIONARY) as dictionary_file:
        dictionary_lines = dictionary_file.readlines()

    dictionary_words = [line.rstrip() for line in dictionary_lines]

    if not dictionary_words:
        raise ValueError('The dictionary is Empty')

    return dictionary_words


def calc_word_value(i_word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    word_value = 0
    for letter in i_word.upper():
        if letter in LETTER_SCORES:
            word_value += LETTER_SCORES[letter]

    return word_value


def max_word_value(i_words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if not i_words:
        i_words = load_words()

    max_word = max(i_words, key=calc_word_value)
    return max_word


def init_find_optimal():

    new_dictionary = {}
    dictionary_words = load_words()

    for word in dictionary_words:
        sign = get_word_signature(word)

        if sign not in new_dictionary:
            new_dictionary[sign] = []

        new_dictionary[sign].append(word)

    SignatureDictionary.dic = new_dictionary


def get_word_signature(word):
    return ''.join(sorted(word)).upper()


def get_substrings_of_exact_score(i_list, i_score):
    current_list = []
    global_list = []
    get_substrings_of_specific_score_r(global_list, list(i_list), current_list, i_score)
    return set(global_list)


def get_substrings_of_specific_score_r(output_list, i_list, i_sub_list, i_score):
    if i_score == 0:
        output_list.append(get_word_signature(i_sub_list))
        return

    if len(i_list) == 0:
        return

    if calc_word_value(i_list[-1]) <= i_score:
        get_substrings_of_specific_score_r(output_list, i_list[:-1], i_sub_list, i_score)
        get_substrings_of_specific_score_r(output_list, i_list[:-1], i_sub_list + [i_list[-1]],
                                           i_score - calc_word_value(i_list[-1]))
    else:
        get_substrings_of_specific_score_r(output_list, i_list[:-1], i_sub_list, i_score)


def find_optimal(i_bunch_of_letters):
    """Find the optimal (highest scoring) word from these letters (including substrings) which is in the dictionary.
    Return it and the score."""

    if not SignatureDictionary.dic:
        init_find_optimal()

    # Calc the maximum score
    max_possible_score = calc_word_value(i_bunch_of_letters)

    # Run from maximum score to 0

    for current_score in reversed(range(max_possible_score + 1)):

        # Find all permutation with this score
        current_score_word_list = get_substrings_of_exact_score(i_bunch_of_letters, current_score)

        # For each permutation check if exist in dic
        for word in current_score_word_list:
            if word in SignatureDictionary.dic:
                identic_signature_words = SignatureDictionary.dic[word]
                maxWord = identic_signature_words[0]
                max_word_value = calc_word_value(maxWord)
                return (maxWord, max_word_value)

    return (None, 0)


if __name__ == "__main__":
    pass # run unittests to validate
