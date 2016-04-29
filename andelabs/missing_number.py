def find_missing(A, B):
    if A == B:
        return 0

    if A != B:
        a = []
        for i in A:
            if i not in B:
                a.append(i)
        for j in B:
            if j not in A:
                a.append(j)
    return a

print find_missing([1, 2], [1, 2, 3])
print find_missing([1, 2, 3], [1, 2, 3, 4])


