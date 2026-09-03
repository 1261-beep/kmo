pole = [67, 34, 89, 72, 47, 99, 12, 41]

for i in pole:
    print(i, end=" ")

min = 0
for i in range(len(pole)- 1):
    if pole[i]<pole[min]:
        min = i



p=pole[i]
pole[i]=pole[0]
pole[0]=p



print()
for i in pole:
    print(i,end=" ")