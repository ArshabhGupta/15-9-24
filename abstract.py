from abc import ABC, abstractmethod
class absclass(ABC):
    def print(self, x):
        print("Passed value:", x)
    @abstractmethod
    def task(self):
        print("We are inside abstract method")

class test_class(absclass):
    def task(self):
        print("We are inside the test class")

obj = test_class()
obj.task()
obj.print(100)