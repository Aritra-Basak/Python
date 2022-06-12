//understanding class and methods 
class Computer:
  def config(self):
    print("Ryzen 3, 8gb , 1TB")
com1 =Computer()
print(type(com1))
com1.config()
class Computer2:
  def __init__(self,cpu,ram):
    self.cpu=cpu
    self.ram=ram
  def inside(self):
    print("config is",self.cpu,self.ram)
com2=Computer2('Ryzen 5',8)
com2.inside()
