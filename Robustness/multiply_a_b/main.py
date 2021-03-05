# range of l = {1 - 500}
# range of b = {1 - 400}
def calcArea(l, b):
    area=l*b;
    return area

def calcArea2(l, b):
    if l<=0 or l>500 or b<=0 or b>400 :
        return "INVALID INPUT"
    
    area=l*b;
        
    return area
    