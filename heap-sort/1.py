#User function Template for python3
from heapq import heapify,heappop
class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        left = (2*i)+1
        right = (2*i)+2
        largest = i
        
        if left < n and arr[largest] <= arr[left]:
            largest = left
        if right < n and arr[largest] <= arr[right]:
            largest = right 
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            self.heapify(arr,n,largest)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n - 1,-1,-1):
            self.heapify(arr,n,i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        size = n
        self.buildHeap(arr,n)
        while size > 0:
            arr[size -1],arr[0] = arr[0],arr[size -1]
            size -= 1
            self.heapify(arr,size,0)