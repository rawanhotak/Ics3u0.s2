def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp
def sort(C): # A very inefficient sorting method!
    for i in range(len(C)):
        for j in range(len(c)):
            if (C[i] < C[j]):
                swap(C, i, j)
A = [4, -1, 7, 3, 9, 0, 11, 2, 14]
sort(A)
print(A)
