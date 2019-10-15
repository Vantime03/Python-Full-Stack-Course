'''
lab24: rain data
'''
import datetime
rain_data = "C:\\Users\\vanbinhluong\\Desktop\\PythonFullStack\\lab24_rain_data\\mt_tabor.rain.txt"
dict_rain_data = {}

with open(rain_data, "r") as rain_data_string:
    line = rain_data_string.readlines()
    # print(len(line))
    for n in range(11, len(line)):
        line_string = line[n]
        rain_count = line_string[14:16]
        rain_count = int(rain_count)
        dict_rain_data[line_string[0:11]] = rain_count
    print(dict_rain_data)

                # date = datetime.datetime.strptime(line_string[0:11], '%d-%b-%Y')


        
        



