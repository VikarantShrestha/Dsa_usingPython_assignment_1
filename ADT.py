class adt:
    def __init__(self, arr):
        self.arr=arr

    def getElByIndx(self,i):
        print(self.arr[i])
    
    def update_El_by_i(self,i,n):
        self.arr[i]=n
    
    def showAll(self):
        print(self.arr)

    def getMax(self):
        print(max(self.arr))

arr=[2,4,6,8]
ob=adt(arr)
ob.getElByIndx(1)
ob.update_El_by_i(1,8)
ob.showAll()
ob.getMax()