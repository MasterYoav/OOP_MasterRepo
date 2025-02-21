#factory - create instances by need
class Dog:
  def speak(self):
    return "Woof!"
  
  def animalFactory():
    return Dog()
  
  dog = animalFactory()
  print(dog.speak())
#abstract Factory - create factories that create instances
class Dog:
  def speak(self):
    return "Woof!"
  
  def AbstractFactory():
    def dogFactory():
      return Dog()
    return dogFactory
  
  factory = AbstractFactory()
  dog = factory()
  print(dog.speak())

#singleton - makes sure theres only 1 instance of class
class Singleton:
  _instance = None
  def __new__(cls):
    if cls.instance is None:
      cls.instance = super(Singleton,cls).__new__(cls)
      return cls.instance
    
s1=Singleton()
s2=Singleton()
print(s1 is s2) #True

#builder- building multy-parameter objects step by step
class CarBuilder:
  def __init__ (self):
    self.color = None
    self.tires = None

    def setColor(self,color):
      self.color = color
      return self
    
car=CarBuilder().setColor("red")
print(car.color)#red

#facade - a simplification class to a complex system
class subsystem:
  def operation(self):
    return "Subsystem operation" #creating complex system

class Facade:
  def __init__(self):
    self.subsystem = subsystem()

  def operation(self):
    return self.subsystem.operation()#simplifying access
  
f = Facade()
print(f.operation()) #"Subsystem operation"

#decorator - adds functionality to an object without changing him
def decorator(func):
  def wrapper():
    print("Adding Features")
    func()
  return wrapper

@decorator
def operation():
  print("Operation")

operation() #Adding Features Operation

#adaptor- adapts 2 classes that do not work the same way
class oldSystem:
  def operation(self):
    return "Old System Operation"
  
class Adapter:
  def __init__(self,oldSystem):
    self.oldSystem = oldSystem

  def newMethod(self):
    return self.oldSystem.operation()
  
Adapter= Adapter(oldSystem())
print(Adapter.newMethod()) #Old System Operation

#flyweight:shares objects instead of duplicating them
class FlyweightFactory:
  _instances={}

  @staticmethod
  def get_instance(key):
    if key not in FlyweightFactory._instances:
      FlyweightFactory._instances[key] = key
    return FlyweightFactory._instances[key]
  
a=FlyweightFactory.get_instance("a")
b=FlyweightFactory.get_instance("a")
print(a is b) #True


#composite - treats objects and compositions of objects uniformly
class Component:
  def operation(self):
    pass #abstact method

class Leaf(Component):
  def operation(self):
    return "Leaf operation"
  
class Composite(Component):
  def __init__(self):
    self.children=[] #hold multiple components

  def add(self,component):
    self.children.append(component)

  def operation(self):
    return "+".join([child.operation() for child in self.children])
  
Composite = Composite()
Composite.add(Leaf())
print(Composite.operation()) #"Leaf operation"


#strategy - defines a family of algorithms, encapsulates each one, and makes them interchangeable
def algorithmA(self):
  return "Algorithm A"
  
class Context:
  def __init__(self,strategy):
    self.strategy = strategy

  def operation(self):
    return self.strategy()
    
context = Context(algorithmA)
print(context.operation()) #"Algorithm A"


class sub:
  def __init__(self):
    self.observers=[]

  def attach(self,observer):
    self.observers.append(observer)
    def notify(self):
      for observer in self.observers:
        observer.update()

class observer:
  def update(self):
    print("notified")

sub=sub()
observer= observer()
sub.attach(observer)
sub.notify() #notified

#Delegate - one object delegates a task to another object
class Delegator:
  def __init__(self,delegate):
    self.delegate = delegate

  def operation(self):
    return self.delegate.operation() #calling the delegation  
  
class ConcreteDelegate:
  def operation(self):
    return "task implementation"
  
d = Delegator(ConcreteDelegate())
d.operation() #task implementation

#iterator - provides a way to traverse a collection of objs
class Iterator:
  def __init__(self,objs):
    self.objs = objs
    self.index = 0
  
def __iter__(self):
  return self
def __next__(self):
  if self.index < len(self.objs):
    value= self.index
    self.index += 1
    return self.objs[value]
  else:
    raise StopIteration
it = Iterator([1,2,3])
for i in it:
  print(i) #1 2 3

#Template - defines the steps of an algorithm and allows subclasses to change the implementation

class Template:
  def step1(self):
    return "step 1"
  def step2(self):
    return "step 2"
  
  def operation(self):
    self.step1()
    self.step2()
  
class ConcreteTemplate(Template):
  def step1(self):
    return "step 1 implementation"  
  def step2(self):
    return "step 2 implementation"
  
t=ConcreteTemplate()
t.operation() #step 1 implementation step 2 implementation


#mvc - separates the concerns of the application
class Model:
  def __init__(self):
    self.data = "data"
  
  def getData(self):
    return self.data
  
class View:
  def showData(self,data):
    print(data)

class Controller:
  def __init__(self,model,view): #controller connects model and view
    self.model = model
    self.view = view

  def updateView(self):
    self.view.showData(self.model.getData()) #updating view with model data

  m=Model()
  v=View()
  c=Controller(m,v)
  c.updateView() #data  
  

