#!venv/bin/python
import argparse
import os

from typing import List, Set, Dict, Tuple, Optional, Union

"""	
Homework ofr Yalantis 1 - 2-3 разных методов для каждого из типов:
str,dict, list, set, tuple 
"""

# argument parser
parser = argparse.ArgumentParser(description="HW1 input: coll - type of collection, s -string ")
parser.add_argument("-coll", "--type_name", help="Type to check", required=True)
parser.add_argument("-s", "--some_string", help="String input", required=False)
args = parser.parse_args()


# class holder for functions
# functions are done in the mode of "rave of an old mare in a dark september night..."
class HolderForFunctions:

    # read file and create text from 2 words of each paragraph adding text
    @staticmethod
    def function_to_use_str(fname: str, added_text: Optional[str]) -> Optional[str]:
        if fname is None or not os.path.isfile(fname):
            return None

        text = ""
        with open(fname) as f:
            for paragraph in f.readline():
                paragraph = paragraph.rstrip()
                if len(paragraph) > 0 and paragraph[0].islower():
                    text += ",".join(paragraph.split()[:2])
                    text += added_text

        return text.capitalize()

    # frequency dictionary from file using special values for punctuation marks
    @staticmethod
    def function_to_use_dict(fname: str, punctuation: Dict[str, int]) -> Optional[Dict[str, str]]:

        if fname is None or not os.path.isfile(fname):
            return None

        frequency_dict = {}
        with open(fname) as f:
            for paragraph in f.readline():
                for letter in paragraph.casefold():

                    if letter in frequency_dict:
                        frequency_dict[letter] += 1
                    else:
                        frequency_dict[letter] = 1

        for punctuation_mark, price in punctuation.items():
            if punctuation_mark in frequency_dict:
                frequency_dict[punctuation_mark] = price * frequency_dict[punctuation_mark]

        return frequency_dict if frequency_dict else None

    # check if text in a file has number and starts with corresponing list value
    @staticmethod
    def function_to_use_list(fname: str, lst: List[str]) -> Optional[str]:

        if fname is None or not os.path.isfile(fname) or lst is None:
            return None

        lst.sort(reverse=True)

        with open(fname) as f:
            for paragraph in f.readline():
                for i in range(len(lst)):
                    if str(i) in paragraph.split() and paragraph.startswith(lst[i]):
                        return "Found strange condition"

        return "Not found strange condition"

    # number of total whitelist words in each paragraph of the file
    @staticmethod
    def function_to_use_set(fname: str, white_list: Set[str]) -> Optional[int]:

        if fname is None or not os.path.isfile(fname) or white_list is None:
            return None

        total_set_words = set()

        with open(fname) as f:

            words_in_paraghraph = set()

            for paragraph in f.readline():
                words = [x.casefold() for x in paragraph.split()]
                for word in words:
                    if word in white_list:
                        words_in_paraghraph.add(word)

            total_set_words.union(words_in_paraghraph)

        return len(total_set_words)

    # number of text in the tuple or count of text in the tuples
    @staticmethod
    def function_to_use_tuple(text: str, options_tuple: Tuple = None, fname: str = None) -> Optional[int]:

        if text is None or options_tuple is None:
            return None

        if fname is None or not os.path.isfile(fname):
            return options_tuple.index(text) if text in options_tuple else None

        with open(fname) as f:
            for paragraph in f.readline():
                if paragraph.startswith(text):
                    return options_tuple.count(text)


if __name__ == "__main__":
    print("Homework 1!")

    TYPES = ('str', 'dict', 'list', 'set', 'tuple')

    print(f"Commandline is -> {args}")

    indexOfType: Optional[int] = HolderForFunctions.function_to_use_tuple(args.type_name,
                                                                          options_tuple=TYPES)
    if indexOfType is None:
        print("There is not such type as {}".format(args.type_name))
        print("List of used types:")
        for item in TYPES:
            print(item, end=", ")
        exit(1)

    FUNCTIONS_NAMES_SET = {'function_to_use_' + x for x in list(TYPES)}

    FUNCTIONS_INPUT = [
        None,
        {",": 1, ":": 2},
        ["aaa", "bbb"],
        {"aaa", "bbb"},
        ("aaa", "bbb"),
    ]
    FUNCTIONS_DICT = {}

    for k, v in zip(TYPES, zip(FUNCTIONS_NAMES_SET, FUNCTIONS_INPUT)):
        FUNCTIONS_DICT[k] = v


    method_to_call = getattr(HolderForFunctions, FUNCTIONS_DICT.get(args.type_name)[0])

    result: Optional[Union[Optional[str],
                           Optional[Dict[str, str]],
                           Optional[str],
                           Optional[int],
                           Optional[int],
                          ]
                    ] = method_to_call(args.some_string, FUNCTIONS_DICT.get(args.type_name)[1])

    if result is None:
        print("The result is None")
    else:
        print(f"The result is -> '{result}'")
