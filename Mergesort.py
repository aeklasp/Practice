def merge(a,b):
    print 'incoming', a, b
    c= []
    i = 0
    j = 0
    k = 0
    #print 'cfirst', c
    while i < len(a) and j < len(b):
         
        if a[i] < b[j]:
            #print 'i', i
            #print 'j', j
            c.append(a[i])
            
            i = i+1
            #print '1', c 
        else:
            c.append(b[j])
            j= j+1
            #print '2', c 
    while i < len(a):
        c.append(a[i])
        i = i+1
        #print '3', c 
    while j < len(b):
        c.append(b[j])
        j= j+1
        #print '4', c
         
    print 'merge' , c    
    return c



def mergesort(alist):
    
       if len(alist) > 1: 
           middle = len(alist)/2
           a = alist[:middle]
           b = alist[middle:]
           #print 'split' 
           #print 'a', a
           #print 'b', b
           a = mergesort(a)
           b = mergesort(b)
           return merge (a,b)

       else:
           return alist

            
alist = [54,26,93,17,77,31,44,55,20]
alist = mergesort(alist)
print alist           