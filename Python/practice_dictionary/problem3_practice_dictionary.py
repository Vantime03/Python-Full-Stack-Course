'''
Problem 3
Average numbers whose keys start with the same letter. Output a dictionary containing those letters as keys and the averages.
d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
unify(d) -> {'a':3, 'b':4, 'c':5}
'''
d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
result_count = {}
result_sum = {}
average= {}
def unify(d):
    for n in d: 
        if result_count.__contains__(n[0]) == True:
            result_count[n[0]] = result_count[n[0]] + 1
            result_sum[n[0]] = result_sum[n[0]] + d[n]
        else:
            result_count[n[0]] = 1
            result_sum[n[0]] = d[n]
    for n in result_sum:
        average[n] = result_sum[n] / result_count[n]    
    return average

def main():
    print(unify(d))

main()