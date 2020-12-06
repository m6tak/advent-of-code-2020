def partI(input_data):
  questions = 'qwertyuiopasdfghjklzxcvbnm'
  counts = []
  for group in input_data:
    group_count = 0
    group_total = ''.join(group)
    for q in questions:
      if q in group_total: group_count += 1
    
    counts.append(group_count)
  
  return sum(counts)

def partII(input_data):
  questions = 'qwertyuiopasdfghjklzxcvbnm'
  counts = []
  for group in input_data:
    group_count = 0
    for q in questions:
      everyone = True
      for person in group:
        if q not in person:
          everyone = False
          break
      if everyone: group_count += 1
    counts.append(group_count)
  return sum(counts)
      





def main():
  lines = open('in.txt').readlines()
  groups = []
  group = []
  for line in lines:
    if len(line) == 0 or line is ' ' or line is '\n': 
      groups.append(group)
      group = []
      continue

    group.append(line.replace('\n', ''))

  groups.append(group)   
  
  print(partI(groups))
  print(partII(groups))


if __name__ == "__main__":
  main()