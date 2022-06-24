def bubble(l):
  a=len(l)
  for i in range(0,a-1):
    swap = False
    for j in range(0,a-i-1):
      if l[j]>l[j+1]:
        l[j]=l[j+1]+l[j]
        l[j+1]=l[j]-l[j+1]
        l[j]=l[j]-l[j+1]
        swap = True
    if swap==False:
      break
  print(l)
n=int(input("Enter the size of the list"))
l=[]
print("Enter the values in the list")
for i in range (1,n+1):
  x=int(input())
  l.append(x)
bubble(l)
