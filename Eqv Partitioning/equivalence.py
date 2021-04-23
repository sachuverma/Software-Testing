# range of  a : 1 -> 20
# range of  b : 0 -> 20
# power function with above boundaries

def power1(a,b):
    if a<1 or b<0 or a>20 or b>20:
        raise ValueError('Out of Range')
    return pow(a,b)

def power2(a,b):
    if a<1 or b<0 or a>20 or b>20:
        raise ValueError('Out of Range')
    return pow(a,b)