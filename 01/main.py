def partI(input_data):
  for n1 in input_data:
    n2 = 2020 - n1
    if n2 in input_data:
      return n1 * n2

def partII(input_data):
  for n1 in input_data:
    for n2 in input_data:
      n3 = 2020 - n1 - n2
      if n3 in input_data:
        return n1 * n2 * n3


def main():
  data_lines = open('in.txt').readlines()
  data = [int(line) for line in data_lines]

  print(partI(data))
  print(partII(data))
  
if __name__ == "__main__":
  main()