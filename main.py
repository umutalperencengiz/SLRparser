#make states shifts reduces and gotos then take input and create a stack , match them.

def error():
    print("INVALID string entered. SYNTAX ERROR!")


def accept():
    print("VALID string entered. ACCEPTED!")





def match(expressionStack,matchStack):


    last_match = len(matchStack)-1
    table = {
         'terminals':    ['id',       '+',       '*',       '(',       ')',       '$',       'E',       'T',       'F'],

                   0:     ['S5',      'error()', 'error()',    'S4',   'error()',    'error()',       1,         2,         3 ],
                   1:     ['error()',     'S6', 'error()',    'error()','error()',    'accept',     'error()',   'error()','error()'],
                   2:     ['error()',      'R2',      'S7',   'error()',   'R2',      'R2',       'error()',   'error()','error()'],
                   3:     ['error()',      'R4',      'R4',   'error()',   'R4',      'R4',       'error()',   'error()','error()'],
                   4:     ['S5',      'error()',     'error',   'S4',  'error()',   'error()',       8,         2,         3   ],
                   5:     ['error()',      'R6',     'R6',   'error()',   'R6'  ,      'R6',       'error()',   'error()','error()'],
                   6:     ['S5',      'error()', 'error()',    'S4',    'error()' , 'error()',   'error()',     9,          3],
                   7:     ['S5',      'error()', 'error()',     'S4',   'error()',     'error()',    'error()',   'error()',    10 ],
                   8:     ['error()',     'S6', 'error()',    'error()',  'S11',     'error()',     'error()',   'error()','error()'],
                   9:     ['error()',     'R1',     'S7',   'error()',  'R1',      'R1',  'error()',   'error()','error()'],
                   10:    ['error()',     'R3',     'R3',   'error()',  'R3',      'R3',     'error()',   'error()','error()'],
                   11:    ['error()',     'R5',     'R5',   'error()',  'R5',      'R5',     'error()',   'error()','error()']}


    if (expressionStack[0] in table.get('terminals')):

        i = table['terminals'].index(expressionStack[0])
        if (table[matchStack[last_match]][i] =='S4'):
            matchStack.append(expressionStack[0])
            expressionStack.remove(expressionStack[0])
            matchStack.append(4)
            print("S4")
            match(expressionStack, matchStack)
        elif(table[matchStack[last_match]][i] =='S5'):
            matchStack.append(expressionStack[0])
            expressionStack.remove(expressionStack[0])
            matchStack.append(5)
            print("S5")
            match(expressionStack, matchStack)
        elif(table[matchStack[last_match]][i] == 'S6'):
            matchStack.append(expressionStack[0])
            expressionStack.remove(expressionStack[0])
            matchStack.append(6)
            print("S6")
            match(expressionStack, matchStack)
        elif (table[matchStack[last_match]][i] == 'S7'):
            matchStack.append(expressionStack[0])
            expressionStack.remove(expressionStack[0])
            matchStack.append(7)
            print("S7")
            match(expressionStack, matchStack)
        elif (table[matchStack[last_match]][i] == 'S11'):
            matchStack.append(expressionStack[0])
            expressionStack.remove(expressionStack[0])
            matchStack.append(11)
            print("S11",matchStack)
            match(expressionStack, matchStack)
        elif (table[matchStack[last_match]][i] == 'R1'):  # 1-) E-> E + T
            if ('+' in matchStack) :
                indexPlus = matchStack.index('+')
                del matchStack[indexPlus:]


            match(expressionStack, matchStack)
            print("R1")
                #print(matchStack)

        elif (table[matchStack[last_match]][i] == 'R2'):  # 2-) E-> T
            del matchStack[last_match-1:]
            matchStack.insert(last_match-1 ,'E')
            if (matchStack[last_match - 2] == 0):
                matchStack.insert(last_match, 1)
            elif (matchStack[last_match - 2] == 4):
                matchStack.insert(last_match, 8)
            match(expressionStack, matchStack)
            print("R2")
        elif (table[matchStack[last_match]][i] == 'R3'):  # 3-) E-> T * F
            if ('*' in matchStack) :
                indexMultiplier = matchStack.index('*')
                del matchStack[indexMultiplier:]
                match(expressionStack, matchStack)
                print("R3")
        elif (table[matchStack[last_match]][i] == 'R4'):  # 4-) T-> F
            del matchStack[last_match-1:]
            matchStack.insert(last_match-1 ,'T')
            if (matchStack[last_match - 2] == 0):
                matchStack.insert(last_match, 2)
            elif (matchStack[last_match - 2] == 4):
                matchStack.insert(last_match, 2)
            elif (matchStack[last_match - 2] == 6):
                matchStack.insert(last_match, 9)
            match(expressionStack, matchStack)
            print("R4")
        elif (table[matchStack[last_match]][i] == 'R5'):  # 5-) F->(E)


            indexParanthesis1 = len(matchStack) - 1 - matchStack[::-1].index('(')
            del matchStack[indexParanthesis1:]

            matchStack.insert(indexParanthesis1, 'F')

            if(')' in expressionStack and '(' in matchStack ):
                expressionStack.remove(expressionStack[expressionStack.index(')')])
                #print("workeed")

            if(matchStack[indexParanthesis1-1]==0):
                matchStack.insert(indexParanthesis1+1, 3)
            elif (matchStack[indexParanthesis1-1] == 4):
                matchStack.insert(indexParanthesis1+1, 3)
            elif (matchStack[indexParanthesis1-1] == 6):
                matchStack.insert(indexParanthesis1+1, 3)
            elif (matchStack[indexParanthesis1-1 ] == 7):
                matchStack.insert(indexParanthesis1+1, 10)
            #print(matchStack)
            #print(expressionStack)
            match(expressionStack, matchStack)
            print("R5")
        elif (table[matchStack[last_match]][i] == 'R6'):  # 6-) F-> id
            del matchStack[last_match-1:]
            matchStack.insert(last_match-1 ,'F')

            if(matchStack[last_match-2]==0):
                matchStack.insert(last_match,3)
            elif (matchStack[last_match - 2] == 4):
                matchStack.insert(last_match, 3)
            elif (matchStack[last_match - 2] == 6):
                matchStack.insert(last_match, 3)
            elif (matchStack[last_match - 2] == 7):
                matchStack.insert(last_match, 10)
            #print(matchStack)
            match(expressionStack, matchStack)
            print("R6")
        elif (table[matchStack[last_match]][i] == 'accept'):
            accept()
        elif (table[matchStack[last_match]][i] == 'error()'):
            error()
           


def main():
    matchStack = [0]
    expression = input("Enter your expression:")

    expressionStack = []
    id = ""

    for literal in expression:

        if literal.isspace():
            pass
        elif (literal.isalnum()):
            id += literal


        elif (literal in "+*()"):
            if (id != ""):
                expressionStack += ['id']
            expressionStack += literal
            id = ""
    if (id != ""):
        expressionStack += ['id']
    expressionStack.append('$')

    #print(expressionStack)
    #rules

    match(expressionStack, matchStack)
    #print(expressionStack)


main()









