digits = '0123456789'
signs = '+-*'

def evaluateEquation(a, b, sign):
  if sign == '+': return a + b
  if sign == '-': return a - b
  if sign == '*': return a * b

def evaluateExpression(exp):
  exp = exp.replace(' ', '').replace('\n', '')
  a = None
  b = None
  sign = None
  index = 0
  opened_brackets = 0
  closed_brackets = 0
  while index < len(exp):
    if exp[index] == ')':
      break

    if a is not None and b is not None and sign is not None:
      a = evaluateEquation(a, b, sign)
      b = None
      sign = None

    if exp[index] in digits:
      if a is None: a = int(exp[index])
      elif b is None: b = int(exp[index])

    if exp[index] in signs:
      if sign is None: sign = exp[index]
    
    if exp[index] == '(':
      opened_brackets += 1
      if a is None: a = evaluateExpression(exp[index+1:])
      else: b = evaluateExpression(exp[index+1:])
      
      while index < len(exp):
        index += 1
        if exp[index] == '(': opened_brackets += 1
        if exp[index] == ')': closed_brackets += 1
        if closed_brackets == opened_brackets: break


    index += 1

  return evaluateEquation(a, b, sign)



def main():
  expressions = open('in.txt').readlines()
  results = []
  for expr in expressions:

    print(f'Evaluating: {expr}')
    res = evaluateExpression(expr)
    results.append(res)
  
  print(sum(results))

if __name__ == "__main__":
  main()