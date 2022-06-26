#removing all the duplicate words in a string.
a = input("Enter a string")
l=[]
l=a.split(" ")
for i in range(0,len(l)):
  for j in range((i+1),len(l)):
    if l[i]==l[j]:
      l[j]= 0
for i in l:
  if i!=0:
    print(i,end=" ")
