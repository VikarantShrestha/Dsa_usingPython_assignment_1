class Array1:
    def __init__(self, max_size):
        self.l = []
        self.max_size = max_size
    
    def CreateArray(self):
        print(f"Enter {self.max_size} elements:")
        for i in range(self.max_size):
            element = input(f" Enter element {i + 1}: ")
            self.l.append(element)
    
    def display(self):
        print(self.l)


max_size = int(input("Enter max size of array: "))
ob = Array1(max_size)
ob.CreateArray()
ob.display()
