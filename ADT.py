class Array1:
    def __init__(self, max_size):
        self.l = []
        self.max_size = max_size
    
    def CreateArray(self):
        print(f"Enter {self.max_size} elements:")
        for i in range(self.max_size):
            element = int(input(f" Enter element {i + 1}: "))
            self.l.append(element)
    
    def showArray(self):
        print(self.l)
    
    def linear_search(self,e):
        for i in range(self.max_size):
            if self.l[i]==e:
                print(f"element found at index : {i}")
                return
        print("element not found")

    def Sorting(self):
        for i in range(self.max_size-1):
            for j in range(0,self.max_size-i-1):
                if self.l[j]>self.l[j+1]:
                    self.l[j],self.l[j+1]=self.l[j+1],self.l[j]
        print(self.l)
    
    def binary_search(self,e):
        beg=0
        end=self.max_size-1
        while(beg<=end):
            mid=(beg+end)//2
            if self.l[mid]==e:
                print(f"element found at index {mid}")
                return
            elif e>self.l[mid]:
                beg=mid+1
            else:
                end=mid-1
        print("element not found")


max_size = int(input("Enter max size of array: "))
ob = Array1(max_size)
ob.CreateArray()
ob.showArray()
ob.linear_search(8)
ob.Sorting()
ob.binary_search(2)