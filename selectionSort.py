class Solution: 
    def select(self, arr, i):
        # Set the current minimum value as the first element
        current_min = i
        # Iterate through the rest of the list to find the minimum value
        for j in range(i+1, len(arr)):
            # If the current element is smaller than the current minimum, update the minimum value
            if arr[j] < arr[current_min]:
                current_min = j
        # Return the minimum value
        return current_min

    def selectionSort(self, arr,n):
        # Iterate through the list
        for i in range(n):
            # Select the minimum value
            min_index = self.select(arr, i)
            # Find the index of the minimum value
            #min_index = arr.index(current_min)
            # Swap the minimum value with the first element
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
