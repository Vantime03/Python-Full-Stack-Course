'''
file name: mad_lib_lab

Lab 2: Mad Libs
Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

Instructions
Search the interwebs for an example Mad Lib
Ask the user for each word you'll put in your Mad Lib
Use string concatenation to put each word into the Mad Lib

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
#variable and read user input
crop = input("Enter a crop (e.g. corn): ")
location = input ("Enter a location (e.g. office): ")
tool = input("Enter a tool (e.g. hammer): ")
number = input("Enter a number (e.g. 10 ): ")
chemical = input("Enter a chemical name (e.g. detergent): ")
emotion = input("Enter an emotional adjective (e.g. sad): ")

#print the story
print(f"\nThe Farmer Story\n\nFarmers work very hard planting wheat and {crop}. They begin by plowing their {location}, and if they don't have a tractor, they use {tool}. Then they plant {crop} seeds, and by the next Fall, they have many acres of {crop}. Tomatoes are harder to raise. They grow on {number} bushes and the farmer sprays them with {chemical}. To keep the bugs off. The easiest things to grow are green {crop}, but the farmer must be careful to make sure worms don't get into his {crop}. Farmers also raise onions, cabbages, lettuce, and {crop}. But no matter what they grow, farmers really lead a {emotion} life.")
