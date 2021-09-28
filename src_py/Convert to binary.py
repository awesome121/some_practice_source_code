from abstract_data_type import Stack

def dividBy2(decNumber):
    remstack = Stack()
    
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
        
    a_string = ''
    while not remstack.isEmpty():
        a_string += str(remstack.pop())
     
    return a_string


decNumber = 96
print(dividBy2(decNumber))
    