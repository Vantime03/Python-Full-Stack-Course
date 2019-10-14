'''
Lab 21: Count Words
Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.

Open the file.
Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts. You can do that with the code below.
# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
    
'''
import string
book= open("C:\\Users\\vanbinhluong\\Desktop\\PythonFullStack\\lab21_count_words\\VERSES_BY_H_BELLOC.txt", encoding="utf-8")
book_dict = {}

def strip_punctuation(book_string):
    for n in string.punctuation:
        book_string = book_string.replace(n, "")
    return book_string

def process_dictionary(book_string):
    word = ""
    first_word = ""
    second_word = ""
    for i in range(len(book_string)):
        if book_string[i] != " ": 
            word += book_string[i]
        elif book_string[i] == " " and first_word == "":
            first_word = word + " "    
            word = ""
        elif book_string[i] != " " and first_word != "" and second_word == "":
            word += book_string[i]
        elif book_string[i] == " " and first_word != "" and second_word == "":
            second_word = word + " "
            word = ""
            if (first_word + second_word) in book_dict:
                count = book_dict.get(first_word + second_word) + 1
                book_dict[first_word+second_word] = count
            else:
                book_dict[first_word+second_word] = 1
            first_word = second_word
            second_word = ""



def finding_top_ten():
    words = list(book_dict.items()) # return a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)
    print("\nHere is the top 10 words in Verse:\n")
    for i in range(min(10, len(words))):
        print(words[i])
    
def main():
    print("Welcom to Word Counts!")
    booktxt = book.read()
    book.close()
    book_string = booktxt.lower() # lower cap words
    book_string = strip_punctuation(book_string) #strip all punctuations
    process_dictionary(book_string) # this will put each unique word into a dictionary start increment
    finding_top_ten()

main()




