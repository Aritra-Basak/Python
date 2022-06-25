#interchanging the 1st and the last element of the list.
a =int(input("Enter the limit of the list"))
l=[]
for i in range(0,a):
  val=int(input("Enter a number"))
  l.append(val)
print("Normally the list is",l)
fe=l[0]
x=len(l)-1
le=l[x]
l.pop(0)
l.insert(0,le)
l.pop(x)
l.insert(x,fe)
print(l)
