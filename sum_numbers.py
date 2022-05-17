"""
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.
"""

def get_sum(a,b):
    
    resp = 0
    
    if a == b:
        resp += a
    
    elif a > b:
        
        for i in range(a - b):
            resp += b
            b += 1
            
        resp += a
        
    else:
        
        for i in range(b - a):
            resp += a
            a += 1
            
        resp += b
            
    return resp

print(get_sum(1,2))
