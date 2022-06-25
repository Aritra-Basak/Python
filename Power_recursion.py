#Finding the power of an number using recursion process.
def power(n,pow):
  if pow==0:
    return 1
  elif pow==1:
    return n
  else:
    return (n*power(n,pow-1)) #calling back the power method from inside of the method itself and multiplying n with its previous power value.

n=int(input("Enter the number"))
pow=int(input("Enter the power of the number"))
print(power(n,pow))
