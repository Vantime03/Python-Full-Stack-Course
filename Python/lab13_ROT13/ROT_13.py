'''
Lab 13: ROT Cipher
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

'''
import string

def encryption(user_input, number_rotation):
    result = ""
    n_index = 0
    for character in user_input: 
        if character != " ":
            placement = string.ascii_lowercase.index(character)
            if placement + number_rotation > 25:
                n_index = abs((placement + number_rotation) - 26)
                placement_with_rot = string.ascii_lowercase[n_index]
            else:
                placement_with_rot = string.ascii_lowercase[placement + number_rotation]
            result = result + placement_with_rot
    return result

def main():
    print("Welcome to ROT 13!")
    user_input = (input("Enter a phrase that you wish to encrypt: ")).lower()
    number_rotation = int(input("Enter the number of rotations that you want to encrypt: "))
    rot_13 = encryption(user_input, number_rotation)
    print(f"Here is the encrypted phrase: {rot_13}")

main()




