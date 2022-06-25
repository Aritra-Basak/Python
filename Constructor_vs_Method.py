#this prog. shows the basic difference in a constructor and a method, like how to pass arguments while creating objects and all.
class School:
  def __init__(self,marks1,marks2,marks3):
    sum=marks1+marks2+marks3
    print("FRom School's constructor")
    print(marks1,"+",marks2,"+",marks3,"=",sum)
class School2:
  def show(self,m1,m2,m3):
    s=m1+m2+m3
    print("From School 2 the total value of sum is",s)
c1=School(1,2,3)
c2=School2()
c2.show(1,2,3)
#We need to pass self everytime when we pass values or arguments in a method or in a constructor cause while creating object of it's respective classes that object is also passed and that object is passed through self as an argument.
