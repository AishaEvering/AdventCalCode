
import re
import os

number_dict = {"one": "1",
               "two": "2",
               "three": "3",
               "four": "4",
               "five": "5",
               "six": "6",
               "seven": "7",
               "eight": "8",
               "nine": "9"}


def findNumbersAsWords(line):
    found_words_dict = {}

    # loop through list of number words
    for key, value in number_dict.items():
        for match in re.finditer(key, line):  # regex find all matches to key
            found_words_dict[match.start()] = key  # add to dict
    return found_words_dict

# return first and last number


def getFirstAndLastNumber(line):
    first_digit = -1
    last_digit = -1

    # regex find all digits
    found_digits = re.findall('\d+', line)

    # if there are digits; find first and last
    if len(found_digits) > 0:
        first_digit = int(str(found_digits[0])[0])
        last_digit = int(str(found_digits[-1])[-1])

    # find all the number words
    found_words_dict = findNumbersAsWords(line)

    # if there are words
    if len(found_words_dict) > 0:
        # get the min/max indexes of number words
        min_word_index = (min(found_words_dict.keys()))
        max_word_index = (max(found_words_dict.keys()))

        # get first/last indexes of digits
        first_digit_index = line.index(str(first_digit))
        last_digit_index = line.rfind(str(last_digit))

        # if most min word index is less than the min digit index set it
        if first_digit_index > min_word_index:
            first_digit = int(number_dict[found_words_dict[min_word_index]])

        # if most max work index is more than the max digit index set it
        if last_digit_index < max_word_index:
            last_digit = int(number_dict[found_words_dict[max_word_index]])

    # concat digits
    return (int(f"{first_digit}{last_digit}"))


input_file_loc = f"{os.getcwd()}/day_1/input.txt"

with open(input_file_loc, "r") as input:
    result = map(getFirstAndLastNumber, input)
    print(sum(list(result)))  # sum up all the values in the list
    input.close()
