


class Sorter:
    def __init__(self):
        pass

    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            curr=arr[i]
            #print(curr, arr)
            j=i-1
            while curr<arr[j] and j>=0:
                arr[j+1]=arr[j] #move left element right
                j-=1
            arr[j+1]=curr
    
    def selectionSort(self, arr):

        for i in range(len(arr)-1):
            min_ind=i
            #print(i, arr)
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min_ind]:
                    min_ind=j
            arr[i],arr[min_ind]=arr[min_ind],arr[i]
    

    def mergeSort(self, arr):
        if len(arr)<=1:
            return arr
        print(arr)
        mid=len(arr)//2
        left,right=arr[:mid],arr[mid+1:]
        self.mergeSort(left)
        self.mergeSort(right)
        
        def merge(l,r):
            t=[]
            print('merge:',l, r)
            while len(l)>0 and len(r)>0:
                if l[0]>r[0]:
                    t.append(l[0])
                    l.pop(0)
                else:
                    t.append(r[0])
                    r.pop(0)
            
            while len(l)>0:
                t.append(l[0])
                l.pop(0)
            
            while len(r)>0:
                t.append(r[0])
                r.pop(0)
            print('merged',t)
            return t

        return merge(left, right)

        


            

            
            

myList=[3,35,57,35,24,4,46,42,64,74,2]
s=Sorter()
s.mergeSort(myList)
print(s.mergeSort(myList))

                
                

