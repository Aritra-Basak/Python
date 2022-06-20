class A():
  def feature1(self):
    print("From class A ")
class B(A):
  def feature2(self):
    print("from class B")
class C():
  def feature3(self):
    print("from class C")
class D(C,A):
  def feature4(self):
    print("from class D")
class E(B):
  def feature5(self):
    print("from class E")
a=A()
a.feature1()
b=B()
b.feature1()
b.feature2()
c=C()
c.feature3()
d=D()
d.feature1()
d.feature3()
d.feature4()
e=E()
e.feature1()
e.feature2()
e.feature5()
