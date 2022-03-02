import csv
import os
import re

INPUT_DIR = os.path.join("data", "shakespeare")
STOPWORDS_PATH = os.path.join(INPUT_DIR, "stopwords.txt")
SHAKESPEARE_PATH = os.path.join(INPUT_DIR, "shakespeare.txt")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "shakespeare_report.csv")

NUM_LINES_TO_SKIP = 246
LAST_LINE_START = "End of this Etext"

# with open(SHAKESPEARE_PATH, 'r',) as in_file:
#     list_file = in_file.readlines()
#     for i in range(len(list_file)):
#         if list_file[i].startswith('THE END'):   #WHY WE DO NOT USE THE END AS ENDING
#             print(i, list_file[i]) # so the ending line start from 124452, but is there any method we can simplify it

# show which line we should ignore
with open(SHAKESPEARE_PATH, 'r',) as in_file:
    list_file = in_file.readlines()
    content = list_file[246:124437]

def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1
str_content = listToString(content)
str_content = str_content.lower()
str_content_2 = re.sub("[^A-Za-z\s]", "", str_content)
str_content_3 = re.sub("\s+", " ", str_content_2)

with open(STOPWORDS_PATH, "r" ,encoding='utf-8') as in_file:
    headline  = in_file.readline()
    list_file = in_file.readlines()
    stop_words = list_file


nonspace_stopwords_2 = []
for i in stop_words:
    nonspace_stopwords_2.append(i.strip())


def word_count(str_):
    word_counts = {}
    for word in str_.split(" "):
        if word not in nonspace_stopwords_2:  # should be same result as nonspace_stopwords_2
            if word in word_counts:
                word_counts[word] = word_counts[word] + 1
            else:
                word_counts[word] = 1
        else:
            pass
    return word_counts


word_count_result = word_count(str_content_3)

word_count_result_2 = sorted(word_count_result.items(), key= lambda x:x[1],reverse=True)
import csv

with open(OUTPUT_PATH,'w', encoding='utf-8', newline='') as out_file:
    csv_writer = csv.writer(out_file)
    header = ['word', 'count']

    data = word_count_result
    csv_writer.writerow(header)
    csv_writer.writerows(data)



#
# def  remove_punctuation(uncleanedcontent):
#     clean_content = ""
#     for i in uncleanedcontent:
#         clean_text = re.sub("[^A-Za-z\s]", " ", i)
#         clean_content.append(clean_text)
#     return clean_content
#
#
# def load_shakespeare_lines(initial_file):
#     "Loads every line in the dataset that was written by Shakespeare as a list of strings."
#     "initial_file must be a list"
#
#     shakespeare_lines = []
#     for i in initial_file:
#         shakespeare_lines.append(i)
#
#     return shakespeare_lines
#
# all_content = load_shakespeare_lines(content)
#
#
#
#
#
# lower_content = get_shakespeare_words(all_content)
#
#
#
# #cleaned_content = remove_punctuation(lower_content)  # anyway I can see the cleanning result? or process?
#
#
# #Normalize all whitespace to single spaces
# def  remove_spaces(uncleanedcontent):
#     text_with_arbitrary_whitespace = []
#     for i in uncleanedcontent:
#         text_with_only_spaces = re.sub("\s+", " ", i)
#         text_with_arbitrary_whitespace.append(text_with_only_spaces)
#     return text_with_arbitrary_whitespace
#
# nospace_str_content = remove_spaces(cleaned_content)
#
#
#
# # convert list element to a string
# # Function to convert
#
# flited_str_content = re.sub('[^A-Za-z\s]', '', str_content)
# flited_str_content_2 = re.sub("\s+", " ", flited_str_content)
#
#
# #Read in the stopwords and apply the same cleaning to them as you did to the other text.
# with open(STOPWORDS_PATH, "r" ,encoding='utf-8') as in_file:
#     headline  = in_file.readline()
#     list_file = in_file.readlines()
#     stop_words = list_file
#
#
# nonspace_stopwords = remove_spaces(stop_words)
#
#
# nonspace_stopwords_2 = []
# for i in nonspace_stopwords:
#     nonspace_stopwords_2.append(i.strip())
#
#
#
#
#
#
#
# "why I cannot remove words from stop words list"
# # for i in stop_words:
# #     nostopwords_str = str_content.replace(i, '')
# #
# # print(nostopwords_str)
#
#
#
#
# #
# def load_stopwords(PATH):
#     """Load the stopwords from the file and return a set of the cleaned stopwords."""
#
#     stopwords = set()
#
#     with open(PATH, 'r',encoding='utf-8') as in_file:
#         list_file = in_file.readlines()
#         for i in list_file:
#             stopwords.add(i.strip())
#     return stopwords
#
# stop_words_revised = load_stopwords(STOPWORDS_PATH)
#
#
# def word_count(str_):
#     word_counts = {}
#     for word in str_.split(" "):
#         if word not in stop_words_revised:  # should be same result as nonspace_stopwords_2
#             if word in word_counts:
#                 word_counts[word] = word_counts[word] + 1
#             else:
#                 word_counts[word] = 1
#         else:
#             continue
#     return word_counts
#
# word_count_result = word_count(flited_str_content_2)
#
# #i) Sort your words by their counts in descending order.
#
# word_count_result = sorted(word_count_result.items(), key= lambda x:x[1],reverse=True)
#
#
#

import csv

with open(OUTPUT_PATH,'w', encoding='utf-8', newline='') as out_file:
    csv_writer = csv.writer(out_file)
    header = ['word', 'count']

    data = word_count_result_2
    csv_writer.writerow(header)
    csv_writer.writerows(data)












#
# def load_shakespeare_lines():
#     "Loads every line in the dataset that was written by Shakespeare as a list of strings."
#
#     shakespeare_lines = []
#
#     # fill this in
#
#     return shakespeare_lines
#
#
# def get_shakespeare_words(shakespeare_lines):
#     """Takes the lines and makes a list of lowercase words."""
#
#     # fill this in
#
#     return words
#
#
# def count_words(words, stopwords):
#     """Counts the words that are not stopwords.
#     returns a dictionary with words as keys and values."""
#
#     word_counts = dict()
#
#     # fill this in
#
#     return word_counts
#
#
# def sort_word_counts(word_counts):
#     """Takes a dictionary or word counts.
#     Returns a list of (word, count) tuples that are sorted by count in descending order."""
#
#     # fill this in
#
#     return sorted_word_counts
#
#
# def write_word_counts(sorted_word_counts, path):
#     """Takes a list of (word, count) tuples and writes them to a CSV."""
#
#        # fill this in
#
#
# if __name__ == "__main__":
#
#     os.makedirs(OUTPUT_DIR, exist_ok=True)
#
#     stopwords = load_stopwords()
#
#     shakespeare_lines = load_shakespeare_lines()
#     shakespeare_words = get_shakespeare_words(shakespeare_lines)
#
#     word_counts = count_words(shakespeare_words, stopwords)
#     word_counts_sorted = sort_word_counts(word_counts)
#
#     write_word_counts(word_counts_sorted, OUTPUT_PATH)
