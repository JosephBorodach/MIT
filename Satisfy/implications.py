import sys

def select_digit(num, i):
    return ((num // (2 **i)) % 2)
def last_n_digits(num, n):
    return [select_digit(num, i) for i in range(n)]

with open(sys.argv[1]) as file :
    formula = file.readline()
    formulaTwo = file.readline()

varsOne = set()
varsTwo = set()
for ch in formula:
    if ch.isupper():
        varsOne.add(ch)

for ch in formulaTwo: 
    if ch.isupper():
        varsTwo.add(ch)

vars = varsOne.union(varsTwo)

if 'T' in vars :
    vars.remove('T')

if 'F' in vars :
    vars.remove('F')

varcount = len(vars)

envcount = 2 ** varcount
envs = (last_n_digits(x,varcount) for x in range(envcount))

envOne = []
envTwo = []
for env in envs :
    dictionary = dict(zip(vars,env))
    dictionary['F'] = False
    dictionary['T'] = True   
    evaluluate = eval(formula, dictionary)
    envOne.append(evaluluate)

    evaluluateTwo = eval(formulaTwo, dictionary)
    envTwo.append(evaluluateTwo)

left_implies_right = True
for i in range(0, len(envOne)) :
    if not(not envOne[i] or envTwo[i]) : 
        left_implies_right = False

right_implies_left = True
for i in range(0, len(envOne)) :
    if not (not envTwo[i] or envOne[i]) : 
        right_implies_left = False

if envOne == envTwo :
    print ('EQUIVALENT')
elif left_implies_right :
    print ('LEFT implies RIGHT')
elif right_implies_left :
    print ('RIGHT implies LEFT')
else : 
    print ('NOT EQUIVALENT') 

#envOne.append(eval(formula, dict(zip(vars,env))) for env in envs)
#envTwo.append(eval(formulaTwo, dict(zip(vars,env))) for env in envs)
#envOne.append(eval(formula, dict(zip(vars,env))))
#envTwo.append(eval(formulaTwo, dict(zip(vars,env))))

#varsTwo = set(ch for ch in formulaTwo if ch.isupper())
#varcountTwo = len(varsTwo)
#envcount = 2 ** varcount
#envsTwo = (last_n_digits(x,varcount) for x in range(envcount))

#envOne = []
#for env in envs : 
#    envOne.append(eval(formula, dict(zip(vars,env))))

#envTwo = []
#for env in envs : 
#    envTwo.append(eval(formulaTwo, dict(zip(vars,env))))