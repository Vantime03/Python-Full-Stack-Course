'''
Lab 18: Peaks and Valleys
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

output:

>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
>>> peaks(data)
[6, 14]
>>> valleys(data)
[9, 17]
>>> peaks_and_valleys(data)
[6, 9, 14, 17]

'''
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def find_peaks(data):
    ls_peak = []
    for n in range(len(data)):
        if n < 2:
            continue
        if data[n-2] == data[n] and data[n-1] > data[n]:
            ls_peak.append(n-1)
    return ls_peak

def find_valleys(data):
    ls_valley = []
    for n in range(len(data)):
        if n < 2:
            continue
        if data[n-2] == data[n] and data[n-1] < data[n]:
            ls_valley.append(n-1)
    return ls_valley

def peak_valley_combine(ls_peak, ls_valley):
    return (ls_peak + ls_valley)
    

def main():
    print("Welcome to peak-and-valley app!\n")
    print(f"Peaks: {find_peaks(data)}")
    print(f"Valleys: {find_valleys(data)}")
    combine = peak_valley_combine(find_peaks(data), find_valleys(data))
    combine.sort()
    print(f"Peaks and Valleys: {combine}")

main()