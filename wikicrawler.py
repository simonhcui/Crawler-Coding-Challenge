import wikipediaapi
import string
import sys
from collections import OrderedDict
from prettytable import PrettyTable

# Takes in a WikipediaPageSection
# Counts every word occurence in individual Wikipedia Sections
def word_count(section_text, word_dict):

    # Parse the text by removing all punctuation and spaces
    no_punctuation = section_text.translate(str.maketrans('', '', string.punctuation))
    no_space = no_punctuation.split()

    for word in no_space:
        if(word not in word_dict):
            word_dict[word] = 1
        else:
            word_dict[word] += 1


# Parses possible arguments that alter the printed result such as how many words to print and what words to exclude
def parse_arguments():
    num_words = 10
    excluded_words = []
    if(len(sys.argv) > 1):
        for argument in sys.argv[1:]:
            if(argument.isdigit()):
                num_words = int(argument)
            else:
                excluded_words.append(argument)

    return num_words, excluded_words


def main(num_words, excluded_words):  
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page('Microsoft')
    
    if(not page_py.exists()):
        print("Missing Wikipedia Page, please check line 38 of source code")
        quit()
        
    section_history = page_py.section_by_title('History')

    # k, v
    # word, number of occurrences
    word_dict = dict()

    my_table = PrettyTable()
    my_table.field_names = ["Word", "# of occurrences"]

    # Count all word occurrences in all subsections of the 'History' section
    for s in section_history.sections:
        word_count(s.text, word_dict)

    ordered_frequency = OrderedDict(sorted(word_dict.items(), key=lambda kv: kv[1], reverse=True))

    num_printed = 0
    for k, v in list(ordered_frequency.items()):
        if(num_printed == num_words):
            break
        if(k not in excluded_words):
            my_table.add_row([k, v])
            num_printed += 1

    print(my_table)

if __name__ == "__main__":
    num_words, excluded_words = parse_arguments()
    main(num_words, excluded_words)



