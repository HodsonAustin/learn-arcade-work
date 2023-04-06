import re
# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():
    """ Read lines in from a file"""

    """ Open file for reading"""
    my_file = open("dictionary.txt")

    """ Create an array"""
    dictionary_list = []

    """ Loop through each word in the document and add it to the list."""
    for line in my_file:

        """ Remove any whitespace at the beginning and end of the line """
        line = line.strip()

        """ Append it to our list"""
        dictionary_list.append(line)

    """ Close the file"""
    my_file.close()

    """ Printing our search method"""
    print("--- Linear Search ---")

    """ Open file for reading"""
    my_file = open("AliceInWonderLand200.txt")

    """ Create a variable to keep track of the line number"""
    line_number = 0

    """ Loop through each line in the file"""
    for line in my_file:

        """ Remove any whitespace at the beginning and end of the line """
        line = line.strip()

        """ Increase the line number """
        line_number += 1

        """ Split the line into a list of words """
        word_list = split_line(line)

        """ Loop through each word in the line """
        for word in word_list:

            """ Convert the word to uppercase """
            word = word.upper()

            """ Check if the word is in the dictionary """
            if word not in dictionary_list:

                """ Print the misspelled word and its line number """
                print(f"Line {line_number} possible misspelled word: {word}")

    """ Close the file """
    my_file.close()

    """ Printing our search method"""
    print("--- Binary Search ---")

    """ Open file for reading"""
    my_file = open("AliceInWonderLand200.txt")

    """ Loop through each line in the file """
    for line in my_file:

        """ Remove any whitespace at the beginning and end of the line """
        line = line.strip()

        """ Increase the line number """
        line_number += 1

        """ Split the line into a list of words """
        word_list = split_line(line)

        """ Loop through each word in the line """
        for word in word_list:

            """ Convert the word to uppercase """
            word = word.upper()

            """ Perform a binary search on the dictionary """
            start = 0
            end = len(dictionary_list) - 1
            while start <= end:
                mid = (start + end) // 2
                if dictionary_list[mid] == word:
                    break
                elif dictionary_list[mid] < word:
                    start = mid + 1
                else:
                    end = mid - 1
            else:

                """ Print the misspelled word and its line number """
                print(f"Line {line_number} possible misspelled word: {word}")

    """ Close the file """
    my_file.close()

if __name__ == '__main__':
    main()
