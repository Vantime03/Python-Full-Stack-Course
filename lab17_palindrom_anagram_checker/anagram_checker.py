'''
lab 17: Anagram checker

Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

Convert each word to lower case (lower)
Remove all the spaces from each word (replace)
Sort the letters of each word (sorted)
Check if the two are equal
>>> enter the first word: anagram
>>> enter the second word: nag a ram
>>> 'anagram' and 'nag a ram' are anagrams
'''
def anagram_checker(word1, word2):
    ls_word1, ls_word2 = remove_spaces_list_sort(word1, word2) 
    if ls_word1 == ls_word2:
        return True
    else: 
        return False   

def remove_spaces_list_sort(word1, word2):
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    ls_word1 = list(word1)
    ls_word2 = list(word2)
    ls_word1.sort()
    ls_word2.sort()
    return ls_word1, ls_word2

def main():
    print("Welcome to anagram checker!")
    word1 = (input("Enter the first word: ")).lower()
    word2 = (input("Enter the second word: ")).lower()
    is_anagram = anagram_checker(word1, word2)
    if is_anagram == True:
        print(f"{word1} and {word2} are anagrams!!!")
    else:
        print(f"\'{word1}\' and \'{word2}\' are NOT anagrams.")

main()
