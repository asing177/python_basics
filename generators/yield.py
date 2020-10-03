def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
  
for value in simpleGeneratorFun():  
    print(value) 


def nextSquare(): 
    i = 1; 
  
    while True: 
        yield i*i                 
        i += 1     

for num in nextSquare(): 
    if num > 100: 
         break    
    print(num) 