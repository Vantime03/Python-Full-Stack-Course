'''
Lab 9: Unit Converter
'''
#unit dictionary
unit_dict = {
  "ft_to_m": 0.3048,
  "mi_to_m": 1609.34,
  "yd_to_m": 0.9144,
  "in_to_m": 0.0254
} # this is represent 1 unit of each to number of units of meter
unit_name = ""

print("Welcome to Unit Converter!")
user_unit_choice = input("Enter the unit for converting to meter (e.g. ft=feet, mi=mile, yd=yard, in=inch):")

if user_unit_choice in ["ft", "mi", "yd", "in"]:
    if user_unit_choice== "ft":
        unit_name = "feet"
    elif user_unit_choice == "yd":
        unit_name = "yards"
    elif user_unit_choice == "in":
        unit_name = "inches"
    elif user_unit_choice == "mi":
        unit_name = "miles"
user_input_number = int(input(f"what is the distance in {unit_name} (enter an number)? "))
result = unit_dict.get(user_unit_choice+"_to_m")
result = result*user_input_number
print(result)
