nilai = set({3,6,9,2,5,7}) 
nilai.update({1,2,4,5,8,9,10})
print(sorted(nilai))

for i in (1,3,4,5,7,8,10):
    nilai.remove(i)
print(nilai)