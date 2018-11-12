from io import StringIO
from greenBerry import greenBerry_eval
import contextlib

def eval(str):         #Function to evaluate postfix expression
    exp=list(str)
    S=[]
    i=0
    while(i<len(exp)):
        if(exp[i].isnumeric()):
            S.append(exp[i])
        else:
            y=int(S[-1])
            S.pop()
            x=int(S[-1])
            S.pop()
            if(exp[i]=='+'):
                S.append(x+y)
            elif(exp[i]=='-'):
                S.append(x-y)
            elif(exp[i]=='*'):
                S.append(x*y)
            elif(exp[i]=='/'):
                S.append(x//y)
            elif(exp[i]=='^'):
                S.append(x**y)
            else:
                pass
        i=i+1
    print(S[0])

def infix_eval(infix_expr): # previous InfixCon
    """
    Convert Infix expression to Postfix and use eval(str) function to evaluate
    the mathematical expression.
    input:
        infix_expr: string containing infix mathematical expression
    referred:
        http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html#fig-moveright
    """
    OP_PRIORITY = {
        "*": 0,
        "/": 0,
        "+": 1,
        "-": 1,
        "(": 2
    }
    postfix_expr=''
    infix_list=list(infix_expr.replace(' ', '')) # clean empty space and convert to list
    op_stack=[]

    for infix_val in infix_list:
        if infix_val.isalnum():
            postfix_expr += infix_val
        elif infix_val == '(':
            op_stack.append(infix_val)
        elif infix_val == ')':
            top_val = op_stack.pop()
            while top_val != '(':
                postfix_expr += top_val
                top_val = op_stack.pop()
        else:
            while (op_stack) and \
                  (OP_PRIORITY[op_stack[-1]] <= OP_PRIORITY[infix_val]):
                postfix_expr += op_stack.pop()
            op_stack.append(infix_val)

    while op_stack:
        postfix_expr += op_stack.pop()

    eval(postfix_expr)


def capture_gb_eval_print(code):
    temp_stdout = StringIO()
    # redirect stdout to catch print statement from eval function
    with contextlib.redirect_stdout(temp_stdout):
        greenBerry_eval(code)
    output = temp_stdout.getvalue().strip()
    return output

def capture_infix_eval_print(code):
    temp_stdout = StringIO()
    # redirect stdout to catch print statement from eval function
    with contextlib.redirect_stdout(temp_stdout):
        infix_eval(code)
    output = temp_stdout.getvalue().strip()
    return output
