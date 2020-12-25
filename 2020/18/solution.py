file = open('input.txt')

expressions = [line.replace(' ', '').strip('\n') for line in file.readlines()]

# print(expressions)

def find_closing_paren(expr, i):
    open_parens = 1
    closed_parens = 0
    for j in range(i + 1, len(expr)):
        if expr[j] == '(':
            open_parens += 1
        elif expr[j] == ')':
            closed_parens += 1
        if open_parens == closed_parens:
            return j
    return None

def evaluate(expr):
    result = None
    prev_op = None

    i = 0
    while i < len(expr):
        token = expr[i]
        if token.isdigit():
            num = int(token)
            if not result:
                result = num
            elif prev_op:
                if prev_op == '+':
                    result += num
                elif prev_op == '*':
                    result *= num
            i += 1
        elif token == '+' or token == '*':
            prev_op = token
            i += 1
        elif token == '(':
            end = find_closing_paren(expr, i)

            value = evaluate(expr[i + 1:end])
            if not result:
                result = value
            elif prev_op:
                if prev_op == '+':
                    result += value
                elif prev_op == '*':
                    result *= value
            i = end + 1
        elif token == ' ':
            i += 1
    
    return result

print(sum(evaluate(expr) for expr in expressions))


def evaluate_v2(expr):
    expr = expr.replace(' ', '')

    tokens = []

    i = 0
    while i < len(expr):
        char = expr[i]
        if char.isdigit() or char == '+' or char == '*':
            tokens.append(int(char) if char.isdigit() else char)
            i += 1
        elif char == '(':
            end = find_closing_paren(expr, i)
            tokens.append(evaluate_v2(expr[i + 1:end]))
            i = end + 1
    

    added_tokens = []

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == '+':
            a = added_tokens.pop()
            b = tokens[i + 1]
            added_tokens.append(a + b)
            i += 2

        else:
            added_tokens.append(token)
            i += 1

    multiplied_tokens = []

    i = 0
    while i < len(added_tokens):
        token = added_tokens[i]
        if token == '*':
            a = multiplied_tokens.pop()
            b = added_tokens[i + 1]
            multiplied_tokens.append(a * b)
            i += 2
        else:
            multiplied_tokens.append(token)
            i += 1       
    
    return multiplied_tokens[-1]

print(sum(evaluate_v2(expr) for expr in expressions))