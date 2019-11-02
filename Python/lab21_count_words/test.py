string1 = "hello world my name is van luong hello world my name is van luong"
word = ""
dict_pair = {}
first_word = ""
second_word = ""

for i in range(len(string1)):
    if string1[i] != " ": 
        word += string1[i]
    elif string1[i] == " " and first_word == "":
        first_word = word + " "    
        word = ""
    elif string1[i] != " " and first_word != "" and second_word == "":
        word += string1[i]
    elif string1[i] == " " and first_word != "" and second_word == "":
        second_word = word + " "
        word = ""
        if (first_word + second_word) in dict_pair:
            count = dict_pair.get(first_word + second_word) + 1
            dict_pair[first_word+second_word] = count
        else:
            dict_pair[first_word+second_word] = 1
        first_word = second_word
        second_word = ""

print(dict_pair)
