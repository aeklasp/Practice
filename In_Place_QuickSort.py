"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort (ar):
    qsort(ar, 0, len(ar) - 1)

def qsort(ar, start, end):
    
    pivot = end  
    i =  start
    if (end-start > 0 ) and (i > -1) and (pivot > -1):   
        
        while i < pivot and (i > -1) and (pivot > -1):
            
            if (ar[pivot] <= ar[i]):# compare pivot with element at position i
                temp = ar[pivot]   #swapping 
                ar[pivot] = ar[i]
                ar[i] = ar[pivot-1]
                pivot -= 1 
                ar[pivot] = temp
                  
            else:
                i += 1 #moving i to right          
        
        qsort(ar,start, pivot-1)#qucik sort of array elements to left of pivot 
        qsort(ar,pivot+1, end)#qucik sort of array elements to right of pivot 
        


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

quicksort(test)
print 'After sorting'
print test