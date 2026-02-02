"""
Q.6. Write a Python program to demonstrate multi-level, multiple inheritance and MRO.
"""
# Multi-level Inheritance: Base → Intermediate → Derived
class Base:
    def greet(self):
        print("Hello from Base")

class Intermediate(Base):
    def greet(self):
        print("Hello from Intermediate")

class Derived(Intermediate):
    def greet(self):
        print("Hello from Derived")

# Mixin class to demonstrate multiple inheritance
class Mixin:
    def mixin_method(self):
        print("Hello from Mixin")

# Multiple Inheritance: MultiDerived inherits from Derived and Mixin
class MultiDerived(Derived, Mixin):
    pass

if __name__ == "__main__":
    # Demonstrate multi-level inheritance
    print("Multi-level Inheritance:")
    derived_obj = Derived()
    derived_obj.greet()  # Expected output: "Hello from Derived"
    
    # Demonstrate multiple inheritance
    print("\nMultiple Inheritance:")
    multi_obj = MultiDerived()
    multi_obj.greet()         # Inherited from Derived (multi-level chain)
    multi_obj.mixin_method()  # Method from Mixin

    # Display the Method Resolution Order (MRO)
    print("\nMethod Resolution Order (MRO) for MultiDerived:")
    for cls in MultiDerived.__mro__:
        print(cls)
