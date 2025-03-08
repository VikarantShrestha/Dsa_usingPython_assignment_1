class circular_queue:
    def __init__(self,size):
        self.l=[None]*size
        self.size=size
        self.front=self.rear=-1

    def insertion(self,e):
        if self.front==(self.rear+1)%self.size:
            print("Queue is already full")
        else:
            if self.front==-1:
                self.front=0
            self.rear=(self.rear+1)%self.size
            self.l[self.rear]=e

    def deletion(self):
        if self.front==-1:
            print("Queue is already empty")
        elif self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size

    def traverse(self):
        if self.front == -1:
            print("Queue is empty")
            return
        i=self.front
        while True:
            print(self.l[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        
ob=circular_queue(4)
ob.insertion(4)
ob.insertion(8)
ob.deletion()
ob.traverse()
        