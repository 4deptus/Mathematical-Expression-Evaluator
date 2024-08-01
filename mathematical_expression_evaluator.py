import operator
import re

# Definition of basic operators
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

# Operator precedence
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
}

# Function to convert expression from infix to postfix form
def infix_to_postfix(expression):
    stack = []
    output = []
    tokens = re.findall(r'\d+\.?\d*|[+/*()-^]', expression)
    
    for token in tokens:
        if token.isnumeric() or re.match(r'\d+\.?\d*', token):
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] in precedence and precedence[token] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    
    return output

# Function to calculate the value of a postfix expression
def evaluate_postfix(postfix):
    stack = []
    
    for token in postfix:
        if token.isnumeric() or re.match(r'\d+\.?\d*', token):
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            result = operators[token](a, b)
            stack.append(result)
    
    return stack[0]

# Expression calculation function
def evaluate_expression(expression):
    postfix = infix_to_postfix(expression)
    result = evaluate_postfix(postfix)
    return result

# Usage example
expression = "3 + 5 * (2 - 8)^2 / 4"
result = evaluate_expression(expression)
print(f"Expression: {expression}")
print(f"Result: {result}")