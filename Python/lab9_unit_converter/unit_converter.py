'''
Lab 9: Unit Converter
'''
#unit dictionary
unit_dict = {
  "m_to_ft": 1/0.3048,
  "m_to_mi": 1/1609.34,
  "m_to_km": 1/1000,
  "m_to_yd": 1.09361,
  "m_to_in": 39.3701,
  "ft_to_m": 0.3048,
  "ft_to_mi": 0.000189394,
  "ft_to_km": 0.0003048,
  "ft_to_yd": 0.333333,
  "ft_to_in": 12,
  "mi_to_m": 1609.34,
  "mi_to_ft": 5280,
  "mi_to_km": 1.60934,
  "mi_to_yd": 1760,
  "mi_to_in": 63360,
  "yd_to_m": 0.9144,
  "yd_to_ft": 3,
  "yd_to_in": 36,
  "yd_to_mi": 0.000568182,
  "yd_to_km": 0.0009144,
  "in_to_m": 0.0254,
  "in_to_km": 2.54e-5,
  "in_to_ft": 0.0833333,
  "in_to_yd": 0.0277778,
  "in_to_mi": 1.5783e-5,
  "km_to_m": 1000,
  "km_to_mi": 0.621371,
  "km_to_ft": 3280.84,
  "km_to_yd": 1093.61,
  "km_to_in": 39370.1
} # this is represent 1 unit of each to number of units of meter


def get_unitname(user_input):
    if user_input in ["ft", "mi", "yd", "in"]:
        if user_input== "ft":
            unit_name = "feet"
        elif user_input == "yd":
            unit_name = "yards"
        elif user_input == "in":
            unit_name = "inches"
        elif user_input == "mi":
            unit_name = "miles"
        elif user_input == "km":
            unit_name = "kilometers"
        elif user_input == "m":
            unit_name = "meters"
        else:
            print("that is an invalid entry! Please try again. ")
        return unit_name

def main():
    print("Welcome to Unit Converter!\n")
    user_unit_input = input("Enter the input unit for converting: (e.g. ft=feet, mi=mile, yd=yard, in=inch, km=kilometer, m=meter): ")
    user_unit_output= input("Enter the output unit for converting: (e.g. ft=feet, mi=mile, yd=yard, in=inch, km=kilometer, m=meter): ")
    user_input_number = int(input(f"Enter the distance in {get_unitname(user_unit_input)} to convert (enter an number): "))
    result = unit_dict.get(user_unit_input+"_to_"+user_unit_output)
    result = result*user_input_number
    print(f"\n{user_input_number} {get_unitname(user_unit_input)} is {result} {get_unitname(user_unit_output)}")

main()
