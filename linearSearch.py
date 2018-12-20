def search(list, n, val):
    i=0
    index=-1
    for i in range(n):
        if list[i]==val:
            index=i
    return index

n = int(input("Enter the number of elements: "))
list =[]

for i in range(n):
    x = int(input("Enter a value: "))
    list.append(x)


val = int(input("Enter the value to search: "))

index = search(list, n, val)

if index==-1:
    print("Value not found")
else:
    print("Value found at ", index)
