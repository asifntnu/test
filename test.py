


class Component:
 def foo(self):
   x =7
   print(x)

class Composite:
 def __init__(self, ob):
  self.ob=ob
  self.ob.foo()

#this is test
m=Composite(Component())