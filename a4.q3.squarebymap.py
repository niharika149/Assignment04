lst=[]
length=int(input("Enter length of the list: "))
for i in range(length):
    element=int(input("Enter element: "))
    lst.append(element)
print(lst)
def square(data):
    return data**2
result=list(map(square,lst))
print(result)