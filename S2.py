nilai = set({3,6,9,2,5,7}) 
nilai.update({1,2,4,5,8,9,10})
print(sorted(nilai))

x = {1,3,4,5,7,8,10}
nilai.difference_update(x)
print(nilai)