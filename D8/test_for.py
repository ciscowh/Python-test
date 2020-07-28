list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]
for x in list1:
    if x in list2:
        print(f'{x} in list1 and List2')
    else:
        print(f'{x} only in List1')
def intersect(list1,list2):
    for x in list1:
        print(f'{x} in list1 and List2') if x in list2 else print(f'{x} only in List1')
if __name__== '__main__':
    intersect(list1,list2)