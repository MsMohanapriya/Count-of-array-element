
def count_array_element(array):
    array_length=len(array)
    max_element=float('-inf')
    element_count=0
    for iterator in range(array_length):
        if(array[iterator]>max_element):
            max_element=array[iterator]
        
    for iterator2 in range(array_length):
        if(array[iterator2]==max_element):
            element_count+=1
            
    return array_length-element_count
  
    
array=list(map(int,input().split()))
print(count_array_element(array))

