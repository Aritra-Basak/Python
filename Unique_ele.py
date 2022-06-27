#creating an unique element lsit in the form of set by using set().
l=[]
x=int(input("Enter the limit of the list"))
print("Enter the numbers in the list")
for i in range(x):
  num=eval(input())
  l.append(num)
print("the unique list is : ",set(l)) #using set function removes all the duplicate elements cause set in python always consist of unique elements
