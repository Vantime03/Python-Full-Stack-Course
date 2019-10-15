'''
Lab 22: Compute Automated Readability Index
Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

ARI Formula

The score is computed by multiplying the number of characters divided by the number of words by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up. Scores greater than 14 should be presented as having the same age and grade level as scores of 14.
'''
import string
book= ("C:\\Users\\vanbinhluong\\Desktop\\PythonFullStack\\lab21_count_words\\Wealth_Against_Commonwealth.txt")

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

def sum_sentences():
    line_count = 0
    with open(book,"r") as book_text:
        book_string = book_text.read()
        for char in range (len(book_string)):
            if book_string[char] in [".", ".\"", "?", "!"]:
                line_count += 1
        return line_count

def sum_character():
    with open(book,"r") as book_text:
        book_string = book_text.read()
        return len(book_string)

def sum_words():
    with open(book, "r") as book_text:
        book_string = book_text.read()
        word = ""
        count = 0
        for char in book_string:
            if char in string.ascii_letters:
                word += char
            elif char not in string.ascii_letters and word != "":
                count += 1
                word = ""
        return count

def calculate_ari(sentence, character, word):
    return round((4.71*(character/word) + 0.5*(word/sentence) - 21.43), 0)

def display_result(ari):
    ari_max = False
    print(f"The ARI for {book[64::]} is {ari}")
    if ari > 14:
        ari = 14
        ari_max = True
    print(f"This corresponds to a {ari_scale[ari]['grade_level']} of difficulty")
    if ari_max == True:
        print(f"that is suitable for an average person greater than 22 years old.")
    else: 
        print(f"that is suitable for an average person {ari_scale[ari]['ages']} years old.")

def main():
    count_sentence = sum_sentences() # count sentences
    count_character = sum_character() # count characters
    count_words = sum_words() # count words
    ari = calculate_ari(count_sentence, count_character, count_words)
    display_result(ari)

main()
