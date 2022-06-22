def fibo(i):
  if i ==1:
    return(0)
  elif i==2:
    return(1)
  else:
   return(fibo(i-1)+fibo(i-2))
l = eval(input("Enter the range"))
for i in range(1,l+1):
  print(fibo(i))
