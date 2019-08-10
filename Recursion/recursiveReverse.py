def RecursiveReverse(L):
    if len(L) <= 1:
        return L
    return L[-1:] + RecursiveReverse(L[:-1])
print(RecursiveReverse([1,2,3,4,5,6,7,8]))