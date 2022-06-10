l=eval(input("Enter the lower limit"))
u=eval(input("Enter the upper limit"))
for i in range(l,u+1):
  flag=0
  if i==1:
      flag=flag+1
  for j in range(2,(i//2)+1):
    if i%j==0:
      flag=flag+1
      break
  if flag==0:
    print(i,"is a prime number")
  else:
    print(i,"is not a prime number")
