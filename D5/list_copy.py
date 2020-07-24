l1 = [4,5,7,1,9,0]
l2 = l1.copy()
l2_sort = sorted(l2)
print(l2_sort)
for i in range(len(l1)):
    print(l1[i],l2_sort[i])
