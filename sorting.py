a=[76, 23, 45, 12, 54, 9] 
print("Original List:", a) 

for i in range(0, len(a)):
    
    
    for j in range(i+1, len(a)):
        print(j)
        
        if a[i] >= a[j]: 
            
            a[i], a[j] = a[j],a[i]
            
print("Sorted List", a)