'''
Using the result from the previous problem, iterate through the dictionary and calculate the average price of an item.
def average(d):
    ...
combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
average(combined) -> 2.2
'''
combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}

def average(combined):
    sum = 0
    for n in combined:
        sum += combined[n]
    print(len(combined))
    return sum/len(combined)

def main():
    print(f"The average price for all fruits is ${round(average(combined), 2)}")
main()

