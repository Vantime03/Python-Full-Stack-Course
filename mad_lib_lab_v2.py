'''
file name: mad_lib_lab

Lab 2: Mad Libs
Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

Instructions
Search the interwebs for an example Mad Lib
Ask the user for each word you'll put in your Mad Lib
Use string concatenation to put each word into the Mad Lib

version 2
Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives,
separated by commas, then use the split(", ") function to store each adjective and later use it in your story.
Add randomness! Use the random module, rather than selecting which adjective goes where in the story.

version 3
Make it a repeatable game. Once you're done prompting the user for words, prompt them for whether they'd like to hear the story.
Use a while loop to keep asking if they'd like to hear the story again until the answer is 'no'.
You could then ask them if they'd like to make another story, and so on.
'''
'''
the story

The Farmer

Farmers work very hard planting wheat and {crop}. They
begin by plowing their {location}, and if they don't have a
tractor, they use {tool}. Then they plant {crop}
seeds, and by the next Fall, they have many acres of {crop}.
Tomatoes are harder to raise. They grow on {number} bushes
and the farmer sprays them with {chemical}. To keep the bugs
off. The easiest things to grow are green {crop}, but the
farmer must be careful to make sure worms don't get into his
{crop}. Farmers also raise onions, cabbages, lettuce, and
{crop}. But no matter what they grow, farmers really lead
a {emotion} life.

'''
# import module
import random

def collectInfo():
    #variable and read user input
    crop = (input("Enter 3 crops separated by commas (e.g. corn, carrot, rice): ")).split(", ")
    location = (input("Enter 3 locations separated by commas (e.g. office, bedroom, kitchen): ")).split(", ")
    tool = (input("Enter 3 tool (e.g. hammer, screwdriver, shovel): ")).split(", ")
    number = (input("Enter 3 numbers (e.g. 10, 11, 12 ): ")).split(", ")
    chemical = (input("Enter 3 chemical name (e.g. detergent, oxygen, vinegar): ")).split(", ")
    emotion = (input("Enter 3 emotional adjective (e.g. sad, angry, frustrated): ")).split(", ")

def tellStory():
    #print the story
    print(f"\nThe Farmer Story\n\nFarmers work very hard planting wheat and {random.choice(crop)}. They begin by plowing their {random.choice(location)}, and if they don't have a tractor, they use {random.choice(tool)}. Then they plant {random.choice(crop)} seeds, and by the next Fall, they have many acres of {random.choice(crop)}. Tomatoes are harder to raise. They grow on {random.choice(number)} bushes and the farmer sprays them with {random.choice(chemical)}. To keep the bugs off. The easiest things to grow are green {random.choice(crop)}, but the farmer must be careful to make sure worms don't get into his {random.choice(crop)}. Farmers also raise onions, cabbages, lettuce, and {random.choice(crop)}. But no matter what they grow, farmers really lead a {random.choice(emotion)} life.")





    # while hearStory in ["yes", "y"]:
    #     #print the story
    #     print(f"\nThe Farmer Story\n\nFarmers work very hard planting wheat and {random.choice(crop)}. They begin by plowing their {random.choice(location)}, and if they don't have a tractor, they use {random.choice(tool)}. Then they plant {random.choice(crop)} seeds, and by the next Fall, they have many acres of {random.choice(crop)}. Tomatoes are harder to raise. They grow on {random.choice(number)} bushes and the farmer sprays them with {random.choice(chemical)}. To keep the bugs off. The easiest things to grow are green {random.choice(crop)}, but the farmer must be careful to make sure worms don't get into his {random.choice(crop)}. Farmers also raise onions, cabbages, lettuce, and {random.choice(crop)}. But no matter what they grow, farmers really lead a {random.choice(emotion)} life.")

collectInfo()

#asking if user want to display the story
hearStory = (input("\n\nWould you like to hear story? (Yes/No)  ")).lower()
while hearStory or hearStoryAgain in ["yes", "y"]:
    tellStory()
    hearStoryAgain = (input("\n\nWould you like to hear story again? (Yes/No)  ")).lower()
    



print("Thank you for using Madlib-The Farmer")




# #test print
# print(crop)
# print(random.choice(crop))


# #print the story
# print(f"\nThe Farmer Story\n\nFarmers work very hard planting wheat and {random.choice(crop)}. They begin by plowing their {random.choice(location)}, and if they don't have a tractor, they use {random.choice(tool)}. Then they plant {random.choice(crop)} seeds, and by the next Fall, they have many acres of {random.choice(crop)}. Tomatoes are harder to raise. They grow on {random.choice(number)} bushes and the farmer sprays them with {random.choice(chemical)}. To keep the bugs off. The easiest things to grow are green {random.choice(crop)}, but the farmer must be careful to make sure worms don't get into his {random.choice(crop)}. Farmers also raise onions, cabbages, lettuce, and {random.choice(crop)}. But no matter what they grow, farmers really lead a {random.choice(emotion)} life.")
