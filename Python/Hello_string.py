a = "hello"
ls = []
word =''
Cap = False

for i in range(len(a)):
    for n in range (len(a)):
        if i == n:
            if a[i] == a[n] and Cap == False:
                word += a[n].upper()
                Cap = True
        else:
            word += a[n]
    ls.append(word)
    word = ''
    Cap = False

print(ls)
    