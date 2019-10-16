'''
Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('catdogcatdog') → True

'''
def Is_count_even(user_input):
    user_input = user_input.replace(" ", "") # eliminate spaces
    word = ""
    dog = 0
    cat = 0
    for char in user_input:
        if char in ["d", "o", "g", "c", "a", "t"]:
            word += char
            if word == "dog":
                dog += 1
                word = ""
            elif word == "cat":
                cat += 1
                word = ""
    if dog == cat:
        return True
    else:
        return False



def main():
    user_input = (input("Enter a string of \"dog\" or \"cat\": ")).lower()
    print(f"Is dog/cat even? {Is_count_even(user_input)}")

main()
