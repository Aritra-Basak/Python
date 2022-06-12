class Students:
  school = "JDS"
  def __init__(self,m1,m2,m3,m4): #constructor
    self.m1=m1
    self.m2=m2
    self.m3=m3
    self.m4=m4
  def avg(self):
    return (self.m1+self.m2+self.m3 + self.m3)/4
  @classmethod
  def getschool(cls):
    print("The school name is ",cls.school)
  @staticmethod
  def info():
    print("This is a Student class")
s1=Students(65,60,57,59)
s2=Students(46,66,56,69)
s3=Students(67,65,63,67)  
Students.getschool()
Students.info()
print("Average of a student in an exam is",s1.avg())
print("Average of a student in an exam is",s2.avg())
print("Average of a student in an exam is",s3.avg())
