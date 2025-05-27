def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp
def sort(C): # A very inefficient sorting method!
    for i in range(len(C)):
        for j in range(len(c)):
            if (C[i] < C[j]):
                swap(C, i, j)
              # insertion sort pseudocode (this is not Python):
# for some array Z of length n:
for i from 1 to n - 1
   for j from 0 to i - 1
      if Z[i] < Z[j] then
         swap(Z, i, j)
