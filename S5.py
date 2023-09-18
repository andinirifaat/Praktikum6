A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
# C=set({})
C={}

print(A.symmetric_difference(B))
print(B^A)
print(A.symmetric_difference(C))
#print(B^C)
print(B.symmetric_difference(C))