class linear_queue:
    def __init__(self,size):
        self.l = [None] * size
        self.front=self.rear=-1
        self.size=size
    def Insertion(self,e):
        if self.rear==self.size-1:
            print("Queue is already full")
        else:
            if self.front==-1:
                self.front=0
            self.rear+=1
            self.l[self.rear] = e
    def Deletion(self):
        if self.front==-1:
            print("Queue is already empty")
        elif self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front+=1
    def Traverse(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.l[i])
        
ob=linear_queue(4)
ob.Insertion(2)
ob.Insertion(4)
ob.Insertion(6)
ob.Insertion(8)
ob.Deletion()
ob.Deletion()
ob.Traverse()