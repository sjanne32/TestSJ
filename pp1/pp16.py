# output: http://codepad.org/2rqaIoH1
# program description
"""
PP 1.6: In the programming language of your choice, write a method that modifies a string using the following rules:

1. Each word in the input string is replaced with the following: the first letter of the word, the count of distinct letters between the first and last letter, and the last letter of the word. For
example, "Automotive parts" would be replaced by "A6e p3s".
2. A "word" is defined as a sequence of alphabetic characters, delimited by any non-alphabetic characters.
3. Any non-alphabetic character in the input string should appear in the output string in its original relative location.
"""

import string

alphabet = string.lowercase + string.uppercase

def transform(sentence):
    final_sentence = ""     # python strings are immutable so create a new string

    new_word    = True      # next char will be a new word
    word_unique = 0         # rather than iterating through the set, keep a count of the current unique internal letters
    word_set    = set()     # use a set for O(1) addition and membership checking

    for char_index, char in enumerate(sentence): # O(N) for a sentence with N characters

        try:
            next_char = sentence[char_index + 1] # O(1) to look up next character
        except IndexError:
            next_char = "" # signals the end of the sentence


        if (char not in alphabet): # non alphabet characters are added in place to final string
            final_sentence += char
            continue # skip rest of loop

        if (next_char not in alphabet) or (next_char == ""):
            if (word_unique > 0): # needed for 1 letter words with no internal letters
                final_sentence += str(word_unique)

            final_sentence += char

            new_word = True # char i+1 will be non-alphabetic or end of sentence
                            # char i+1 will be added to final and skip remaining logic
                            # char i+2 will use this for determining a new word
                            # cannot go in above conditional because needed for end of sentence
            word_unique = 0
            word_set.clear() # clear the set for the next word's membership testing

            continue # skip rest of loop


        if new_word == True: # first char of word is added without any membership logic
            final_sentence += char
            new_word = False
        else:
            letter_exists = char in word_set # set() O(1) memebership test
            if (not letter_exists): # if char is unique, increment uniqueness counter
                word_unique += 1
                word_set.add(char) # O(1) set addition, might as well put it in the conditional

    return final_sentence


def run_tests(cases, debug):
    results = []
    for ci, case in enumerate(cases):
        case_input, case_expected_output = case
        case_output = transform(case_input)
        if (debug):
            is_correct = "correct" if (case_expected_output == case_output) else "incorrect"
            print """Test case #%d (%s)\n\tInput: %s\n\tOutput: %s\n\tExpected: %s\n""" % (ci, is_correct, case_input, case_output, case_expected_output)
        results.append(case_output == case_expected_output)
    return results




if __name__ == "__main__":
    test_cases = [
        ("",""),
        ("a","a"),
        ("locomotives","l7s"),
        ("automotive parts","a6e p3s"),
        ("mis-represented youths","m1s-r6d y4s"),
        ("a small-ish rabbit","a s3l-i1h r3t"),
        ("don't eat that cookie","d1n't e1t t2t c3e"),
        ("    confused      yet?    !", "    c6d      y1t?    !"),
    ]

    test_results = run_tests(test_cases, True)

    if (not all(test_results)):
        print "tests failed"
    else:
        print "tests succeeded"