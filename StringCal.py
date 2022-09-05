import re
def calculator(s):
    sum=0

    result = [int(d) for d in re.findall(r'-?\d+', s)]
    

    for i in result:
        if i<0:
            return "negative not allowed"
            break
        
        else:
            sum+=i


    return sum
    

calculator('-5+2y')