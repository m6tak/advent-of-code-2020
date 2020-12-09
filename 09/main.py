def constructSumFromArray(needle, haystack):
  for n in haystack:
    if (needle - n) in haystack: return True

  return False

def partI(input_data):
  index = 25
  while index < len(input_data):
    number = input_data[index]
    if not constructSumFromArray(number, input_data[(index - 25):index]): return number
    index += 1
  
  return -1

def partII(input_data):
  needle = 27911108
  numbers = []
  for i in range(len(input_data)):
    index = i
    while index < len(input_data):
      numbers.append(input_data[index])
      if len(numbers) >= 2 and sum(numbers) == needle:
        print("Found")
        sorted_numbers = sorted(numbers)
        return sorted_numbers[0] + sorted_numbers[-1]

      if sum(numbers) > needle:
        numbers = [input_data[index]]

      index += 1

def main():
  lines = open('in.txt').readlines()
  numbers = [int(line) for line in lines]

  print(partI(numbers))
  print(partII(numbers))

if __name__ == "__main__":
  main()