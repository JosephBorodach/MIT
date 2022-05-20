with open("test.txt", "r") as file: 
    open_file = file.read()
    
satisfied = 0 
not_satisfied = 0 #still need to check if it is alpha!!!!
distinct = {x.rstrip() for x in open_file} #distinct = (variable for variable in open_file if not variable in distinct)
length = len(distinct) #list

for i in range(0,2**length): 
    binary = bin(i) #binary_length = len(distinct)
    digits = f"binary:length" #digits = f"bin(i):length    
    print(digits)
    true_false = ()