def findAllIndicesOfInstruction(instruction_set, instruction):
  index = 0
  indices = []
  for i in instruction_set:
    if i['name'] == instruction: indices.append(index)
    index += 1
  
  return indices

def executeProgramOnce(instruction_set):
  acc_value = 0
  index = 0
  executed_indices = []
  termination_message = 'Natural termination'
  while index < len(instruction_set):
    if index in executed_indices:
      termination_message = "Infinite loop"
      break
    executed_indices.append(index)
    instruction = instruction_set[index]
    
    sign = 1
    if instruction['value'][0] is '-': sign = -1

    if instruction['name'] == 'nop':
      index += 1
      continue

    if instruction['name'] == 'acc':
      acc_value += int(instruction['value'][1:]) * sign
      index += 1

    if instruction['name'] == 'jmp':
      index += int(instruction['value'][1:]) * sign
 
  return {
    'acc_value': acc_value,
    'termination_message': termination_message 
  }


def partI(input_data):
  return executeProgramOnce(input_data)

def partII(input_data):
  jmp_indices = findAllIndicesOfInstruction(input_data, 'jmp')
  nop_indices = findAllIndicesOfInstruction(input_data, 'nop')
  for index in jmp_indices:
    input_data[index]['name'] = 'nop'
    res = executeProgramOnce(input_data)
    if res['termination_message'] == 'Natural termination':
      return res
    input_data[index]['name'] = 'jmp'
  
  for index in nop_indices:
    input_data[index]['name'] = 'jmp'
    res = executeProgramOnce(input_data)
    if res['termination_message'] == 'Natural termination':
      return res
    input_data[index]['name'] = 'nop'
  
  return None


def main():
  lines = open('in.txt').readlines()
  instruction_set = [{'name': line.split()[0], 'value': line.split()[1]} for line in lines]
  print(partI(instruction_set))
  print(partII(instruction_set))


if __name__ == "__main__":
  main()