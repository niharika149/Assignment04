lst=[]
length=int(input("Enter length of the list: "))
for i in range(length):
    element=int(input("Enter element: "))
    lst.append(element)
print(lst)
def triple(data):
    return data*3
result=list(map(triple,lst))
print(result)