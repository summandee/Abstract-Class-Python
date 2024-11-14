# Abstract-Class-Python
An abstract class in Python is a class that contains one or more abstract methods.
# what is abstract class in python and why its necessory?
 ### In Python, an abstract class is a class that cannot be instantiated on its own and is designed to be subclassed. Abstract classes serve as a blueprint for other classes and can contain abstract methods that must be implemented by its subclasses. They are defined using the abc module in Python, which stands for Abstract Base Classes.


# Key Points about Abstract Classes in Python:
1. Definition:
- An abstract class in Python is a class that contains one or more abstract methods.
- Abstract methods are methods declared in the abstract class but do not contain an implementation.
2. abc Module:
- Abstract classes are created using the abc module, which provides the infrastructure for defining abstract base classes.
3. Abstract Methods:
- Abstract methods are declared using the @abstractmethod decorator from the abc module.
- Subclasses of an abstract class must provide an implementation for all abstract methods defined in the abstract class.
4. Enforcing a Contract:
- Abstract classes help enforce a contract between the base class and its subclasses.
- They define a common interface that all subclasses must adhere to.
5. Polymorphism:
- Abstract classes promote polymorphism, allowing different classes to share a common interface but provide different implementations.
6. Why Abstract Classes are Necessary:
- Encapsulation and Structure:
  Abstract classes help in structuring code by defining a common interface that subclasses must implement. This promotes code 
  organization and encapsulation.
- Enforcement of Methods:
  Abstract classes ensure that certain methods are implemented by all subclasses, providing a level of predictability and consistency in 
  the behavior of related classes.
- Flexibility and Extensibility:
  By using abstract classes, you can define a basic structure that can be extended and customized by subclasses. This allows for 
  flexibility in adding new functionalities while maintaining a consistent interface.
- Promoting Code Reusability:
  Abstract classes encourage code reusability by providing a template that can be shared among multiple related classes.
### In summary, abstract classes in Python are necessary for defining a common structure and ensuring that subclasses adhere to a ### specific contract. They help in organizing code, promoting consistency, and facilitating code reuse and extensibility in object-oriented programming.
