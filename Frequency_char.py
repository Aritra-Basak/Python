#frequency of each characters in a string.
a = input("Enter a string to check")
dic= {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print("The frequency of each characters in the string is:")
print (dic)
