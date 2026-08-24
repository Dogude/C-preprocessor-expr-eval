import re

class Types:
    OPERAND = 1
    OPERATOR = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    
def c_eval(expression):

    # expression is a string
    # this function returns True or False based on the evaluation of the expression
    stringList = re.findall(r'\b(defined)\b|(\w+)|(&&|\|\||==|!=|\(|\)|\
                            &|\||!|<<|>>|<|>|>=|<=|\+|-|/|%|\*|^|~|.+?)', expression)
    
    # convert list of tuples to list of strings
    tokens = []
            
    for tup in stringList:
        for item in tup:
            if item != '' and item != ' ':
                tokens.append(item)

    state = Types.OPERAND
    
    par = []
    # syntax checking & parsing
    for i in range(len(tokens)): 
        t = tokens[i]
        match state:
            case Types.OPERAND:
                if t == '!':
                    pass
                elif t == 'defined':
                    state = Types.D
                elif t == '-':
                     tokens[i] = '-u' # convert unary sub
                     state = Types.C
                     
                elif t == '+':
                    tokens[i] = '+u'  # convert unary add
                    state = Types.C
                elif t == '~':
                    state = Types.C
                elif t == '(':
                    par.append(1)
                elif t.isnumeric() or t.isidentifier():
                    state = Types.OPERATOR                   
                else:
                    print("error in expression1")
                    return 
            
            case Types.D:
                if t == '(':
                    state = Types.E
                elif t.isidentifier():
                    state = Types.OPERATOR
                else:
                    print("error in expression2")
                    return 
            
            case Types.E:
                if t.isidentifier():
                    state = Types.G
                else:
                    print("error in expression3")
                    return 
            
            case Types.G:
                if t == ')':
                    state = Types.OPERATOR
                else:
                    print("error in expression4")
                    return 
            
            case Types.C:
                if t == '!':
                    pass
                elif t == '-':
                     tokens[i] = '-u' # convert unary sub
                elif t == '+':
                    tokens[i] = '+u'  # convert unary add
                elif t == '~':
                    pass
                elif t == '(':
                    state = Types.OPERAND
                    par.append(1)
                elif t.isnumeric() or t.isidentifier():
                    state = Types.OPERATOR
                else:
                    print("error in expression5")
                    return 
            
            case Types.OPERATOR:
                if t in ('&&' , '||' , '==' , '!=' , '&' ,  '|'  , '<<' , '>>' , '<' , '>' , '>=' , '<=' ,  '+' , '-' , '/' , '%' , '*' , '^'):
                    state = Types.OPERAND
                elif t == ')':
                    if par is None:
                        print("error in expression6")
                        return
                    par.pop()    
                else:
                    print("error in expression7")
                    return
    
    if state != Types.OPERATOR:     
        print("error in expression8")
        return
    elif par:
        print("error in expression9")
        return

     
    # Precedence dictionary
    precedence = {
        'defined': 14, 
        '~': 14,
        '-u': 14,  
        '+u': 14,  
        
        '!': 14,
        '*': 13,
        '/': 13,
        '%': 13,
    
        
        '+': 12,
        '-': 12,
    
        
        '<<': 11,
        '>>': 11,
    
        
        '<': 10,
        '>': 10,
        '<=': 10,
        '>=': 10,
    
        
        '==': 9,
        '!=': 9,
    
        
        '&': 8,
        '^': 7,
        '|': 6,
    
        
        '&&': 5,
        '||': 4
    }

    output = []
    stack = []

    # build postfix expression AST
    for token in tokens:
        if (token.isidentifier() or token.isnumeric()) and token != 'defined':
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '(' from the stack
        elif token in precedence:
            while (stack and stack[-1] != '(' and
                   precedence[stack[-1]] > precedence[token]):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    
    # evaluate postfix expression
    eval_stack = []
    for token in output:
        if token.isnumeric():
            eval_stack.append(int(token))
        elif token.isidentifier() and token != 'defined':
            eval_stack.append(0)  # Undefined identifiers are treated as 0
        elif token == '+':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(a + b)
        elif token == '-':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(a - b)           
        elif token == '*':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(a * b)
        elif token == '/':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(a // b)
        elif token == '%':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(a % b)
        elif token == '<<':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(a << b)
        elif token == '>>':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(a >> b)
        elif token == '<':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(int(a < b))
        elif token == '==':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(int(a == b))
        elif token == '!=':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(int(a != b))
        elif token == 'defined':
            a = eval_stack.pop()           
            eval_stack.append(0)
        elif token == '>':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(int(a > b))
        elif token == '<=':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(int(a <= b))
        elif token == '>=':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(int(a >= b))
        elif token == '&&':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(int(a and b))
        elif token == '||':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(int(a or b))
        elif token == '&':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(a & b)
        elif token == '|':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(a | b)
        elif token == '!':
            a = eval_stack.pop()
            eval_stack.append(int(not a))
        elif token == '+u':
            a = eval_stack.pop()
            eval_stack.append(+a)
        elif token == '-u':
            a = eval_stack.pop()
            eval_stack.append(-a)
        elif token == '~':
            a = eval_stack.pop()
            eval_stack.append(~a)
        elif token == '^':
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(a ^ b)
    
    result = eval_stack.pop()
    output = True if result is None else result
    return bool(output)


#if
expr = "10 - 10 + 2 - 2"

print(c_eval(expr))
