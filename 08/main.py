def executeProgramOnce(instruction_set):
  acc_value = 0
  index = 0
  executed_indices = []
  while index not in executed_indices:
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
 
  return acc_value

def partI(input_data):
  return executeProgramOnce(input_data)


def main():
  lines = open('in.txt').readlines()
  instruction_set = [{'name': line.split()[0], 'value': line.split()[1]} for line in lines]
  print(partI(instruction_set))


if __name__ == "__main__":
  main()