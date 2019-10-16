import numpy as np

def printList(lst):
    pre=[]
    product=1
    for a in lst:
        pre.append(product)
        product=product*a
    
    after=[]
    product=1
    for i in lst[::-1]:
        after.append(product)
        product=product*i
    after.reverse()
    
    answer=np.multiply(pre,after)
    print(answer)
    
    
printList([1,2,3,4,5])