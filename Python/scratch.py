def diamond(n):
    if n % 2 == 0 or n < 0:
        return
    else:
        whole = n // 2
        result = ''
        for i in range(n):
            if i < whole:
                result += ' '
            else:
                result += '*\n'
        return result

a = diamond(3)
print(a)