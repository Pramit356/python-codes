import sys

sys.setrecursionlimit(2000)


def sort(list, n):
    for i in range(n):
        for j in range(i,n):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
    return list



def binSearch(list, n, val):
    i=0
    j=n-1
    index=-1
    while(i<=j):
        mid = (i+j)//2
        if list[mid]>val:
            j = mid-1
        elif list[mid]<val:
            i = mid+1
        else:
            index = mid
            break
    return index


n = int(input("Enter the number of elements: "))
list =[]

for i in range(n):
    x = int(input("Enter a value: "))
    list.append(x)

list = sort(list, n)

print(list)
val = int(input("Enter the value to search: "))

index = binSearch(list, n, val)

if index==-1:
    print("Value not found")
else:
    print("Value found at ", index)
