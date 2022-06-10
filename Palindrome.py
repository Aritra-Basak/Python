s= input("Enter a string")
print(s[0:])
print(s[::-1])
if s[0:]==s[::-1]:
  print("Palindrome")
else:
  print("Not palindrome")
