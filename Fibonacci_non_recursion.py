l = int(input("enter the limit"))
f1=0
f2=1
f=0
print(f1)
print(f2)
for i in range (3,l+1):
  f=f1+f2
  print(f)
  f1=f2
  f2=f
