#Calculating the upper and lower case characters.
str1=input("Enter the string")
lower=0
upper=0
for i in str1:
  if i.isupper():
    upper=upper+1
  else:
    lower=lower+1
print("In ",str1,"the number of uppercase characters are:",upper,"and lower is:",lower)
