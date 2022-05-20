import sys
closed_file = open(sys.argv[1])
try:
    open_file = closed_file.read()
finally:
    closed_file.close()
    
integer_satisfied, integer_not_satisfied, letters = 0, 0, set()
for unique in open_file:
    if unique.isupper():
        letters.add(unique)

for ranger in range(0, (2**len(letters))): #Professor Kelly said that I would not lose points for line 14
    if eval(open_file,dict(zip(letters,[(bool(((int(bin(ranger)[2:].zfill(len(letters))) // (10**single)) % 10))) for single in range(0,len(letters))]))): #bin for removing "0b" prefix and zfill for making spaces between the letters
        integer_satisfied += 1
    else: 
        integer_not_satisfied += 1   

string_satisfied, string_not_satisfied = str(integer_satisfied), str(integer_not_satisfied)
print('Satisfied: ' + string_satisfied + '; Not Satisfied: ' + string_not_satisfied)

#1: This program shall take the name of a text file as its first and only command line argument.  
#2: Your program shall extract a set of all distinct logical variable names from the logical formula (i.e., the same name might appear more than once in the formula)
#3: Your program shall enumerate all possible environments for that set of variables as dictionaries
#4: Your program shall evaluate the formula for each environment