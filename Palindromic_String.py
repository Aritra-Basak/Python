#checking whether a string is palindrome or not.
s = (input("enter a string"))
if s==s[::-1]:
  print("Palindrome")
else:
  print("Not palindrome")
rev= ''.join(reversed(s)) #method 2 to check a string is palindrome or not
print("reversed string is ",rev)
if (s==rev):
  print("Palindrome")
else:
  print("Not palindrome")
