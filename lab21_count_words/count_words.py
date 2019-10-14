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

def main():
    print("Welcom to Word Counts!")
    booktxt = book.read()
    book.close()
    book_string = booktxt.lower()

    #strip all punctuations
    for n in string.punctuation:
        book_string = book_string.replace(n, "")
    
    # this will put each unique word into a dictionary start increment
    word = ""
    for n in book_string: 
        if n != " ":
            word += n
        elif n == " ":
            if word in book_dict: # verify of word is in the existing dict
                count = book_dict.get(word) + 1
                book_dict[word] = count
                word = ""
            else: 
                book_dict[word] = 1
                word = ""

    words = list(book_dict.items()) # return a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(words))):
        print(words[i])

main()




