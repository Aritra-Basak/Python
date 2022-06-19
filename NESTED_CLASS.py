class Student:
  def __init__(self,name, roll):
    self.name=name
    self.roll=roll
  def show(self):
    print(self.name,self.roll)
  class laptop:
    def __init__(self,brand,cpu):
      self.brand=brand
      self.cpu=cpu
    def show(self):
      print(self.brand,self.cpu)
s1=Student('Aritra',80)
s1.show()
s1.lap=s1.laptop('Asus','Ryzen5')
s1.lap.show()
  
