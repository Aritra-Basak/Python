#finding the 2nd largest element inside a list by using sorting and printing the 2nd last element.
n = eval(input())
score=[]
for i in range(1,n+1):
  x= eval(input())
  score.append(x)
print(sorted(list(score))[-2])
