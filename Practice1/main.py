
def priority(operation):
    if operation == '+' or operation == '-':
        return 1
    if operation == '*' or operation == '/':
        return 2
    return 0

def in2post(expression):

    expression = expression.replace(" ", "") # remove spaces for proper calculation
    
    output = [] # stack 4 output
    operators = [] # stack 4 operators (more like array but whatever)
    
    for char in expression: # reading expression and working with it

        if char.isalnum(): # num spotted
            output.append(char)
        elif char == '(': # bracket open
            operators.append(char)
        elif char == ')':  # bracket close
            while operators and operators[-1] != '(': # removing operations from stack till '('
                output.append(operators.pop()) # removed operator added to output
            operators.pop() 
        else:  
            while (operators and priority(operators[-1]) >= priority(char)): # checking operators for priority (current + last)
                output.append(operators.pop())
            operators.append(char)
            output.append(' ') # dlya chitabelnosti

    while operators: # ya ustal na english pisat commenti no UTF-8 ne daet na russkom
        output.append(operators.pop()) # esli operatori eshe est' to ih znacheniya udalyam i dobavlyam v stack vivoda
    
    return ''.join(output) # bez join vigladit kak massiv

def calculatein2post(expression):
    expi2p = in2post(expression)
    num = ""
    numint = 0
    numint2 = 0
    oper = []
    print(expi2p)
    for char in expi2p:
        if char.isalnum():
            num += char
        elif char == ' ' and numint == 0:
            numint = int(num)
            num = ""
        elif char == '+':
            numint2 = int(num)
            num = ""
            numint += numint2
        elif char == '*':
            numint2 = int(num)
            num = ""
            numint *= numint2
        elif char == '/':
            numint2 = int(num)
            num = ""
            numint /= numint2
        elif char == '-':
            numint2 = int(num)
            num = ""
            numint -= numint2
            
    print(numint)


if __name__ == "__main__":
    expression = "(10 + 2) * 2"
    postfix_expression = in2post(expression)
    print(f"Reverse Polish Notation of '{expression}' is {postfix_expression}")\
    
    result = calculatein2post(expression)
