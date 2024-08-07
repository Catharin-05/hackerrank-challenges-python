thickness = int(input()) #enter an odd number

H = 'H'
for i in range(thickness):
    line = H*i
    width = thickness-1
    print(line.rjust(width)+H+(line.ljust(width)))
for i in range(thickness+1):
    line = H*thickness
    print(line.center(thickness*2)+line.center(thickness*6))
for i in range((thickness+1)//2):
    line = H*thickness
    print((line*5).center(thickness*6))    
for i in range(thickness+1):
    line = H*thickness
    print(line.center(thickness*2)+line.center(thickness*6))
for i in range(thickness): 
    line = H*(thickness-i-1)
    print(((line).rjust(thickness)+H+(line).ljust(thickness)).rjust(thickness*6))
