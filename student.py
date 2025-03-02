class student:

    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    
    def showdata(self):
        print(self.name)
        print(self.roll)

    def showmarks(self):
        print(self.marks)


name = input("Enter student name : ")
roll = int(input("Enter roll : "))
marks = list(map(int, (input("Enter marks seperated by space : ").split())))

ob=student(name, roll, marks)
ob.showdata()
ob.showmarks()