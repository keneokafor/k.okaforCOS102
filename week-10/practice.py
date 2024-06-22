# Python program to demonstrate error if we
# forget to invoke __init__() of the parent.

class A:
    def __init__(self, n = 'Emmanuel Abbah'):
        self.name = n
        
class B(A):
    def __init__(self, roll):
        # Calling the parent's __init__ method
        super().__init__()
        self.roll = roll

# Object Instance
obj = B(123)
print(obj.roll)
print(obj.name)
