n = int(input())
score=[]
for i in range(1,n+1):
  x=int(input())
  score.append(x)
max=score[0]
for j in range(1,len(score)) :
  if max<score[j]:
    smax=max
    max=score[j]
  else:
    smax=score[j]
print(smax,"Is the 2nd largest elememt")
