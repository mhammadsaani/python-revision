from typing import List

class Sorting:
    
    
    # helper for selection sort
    def get_minimum(self, starting_idx: int, arr: List) -> int:
        _min = starting_idx
        for idx in range(starting_idx, len(arr)):
            if arr[idx] <= arr[_min]:
                _min = idx 
        return _min      
              
    # helper method for selection sort
    def swap(self, idx1: int, idx2: int, arr: List) -> int:
        temp = arr[idx1]
        arr[idx1] = arr[idx2]
        arr[idx2] = temp
    
    def selection_sort(self, arr: List) -> List:  # n sqare for worst, average and best
        for idx in range(len(arr)):
            min_idx = self.get_minimum(idx, arr)
            self.swap(idx, min_idx, arr)
        return arr

    def bubble_sort(self, arr: List) -> List:  # n square in worst and average but n in best case
        swap = 0
        for idx in range(len(arr)):
            for idx2 in range(len(arr) - idx - 1):
                if arr[idx2] > arr[idx2+1]:
                    self.swap(idx2, idx2+1, arr)
                    swap = 1
            if swap == 0:
                break
        return arr
    
    def insertion_sort(self, arr: List) -> List:  # n square average and worst case but n for best
        for idx in range(1, len(arr)):
            current_idx = idx
            while current_idx != 0:
                if arr[current_idx] < arr[current_idx-1]:
                    self.swap(current_idx, current_idx-1, arr)
                    current_idx -= 1
                else:
                    break
        return arr
    
    

arr = [3,1,4,5, 0,1002, -1]
sorted_arr = [1,2,3,4]
sorting = Sorting()
# print(sorting.selection_sort(arr))
# print(sorting.bubble_sort(sorted_arr))
# print(sorting.bubble_sort(arr))
print(sorting.insertion_sort(arr))
            