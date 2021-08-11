def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
