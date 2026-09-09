class MedianFinder:

    def __init__(self):
        self.arr=[]


    def addNum(self, num: int) -> None:
        self.arr.append(num)
        if(len(self.arr)>1):
            # back push to sorting pos
            i=len(self.arr)-2
            while(num<self.arr[i]):
                tmp=nums[i]
                nums[i]=num
                nums[i+1]=tmp
                i-=1


    def findMedian(self) -> float:
        length=len(self.arr)
        idx=length//2
        if(length%2==0):
            
            #print(idx)
            return (self.arr[idx]+self.arr[idx-1])/2

        else:
            return self.arr[idx]
        
        
