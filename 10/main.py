def findNextAdapter(current_jolts, used_adapters, input_data):
  results = []
  for adapter in input_data:
    diff = adapter - current_jolts
    if diff <= 3 and diff >= 1 and adapter not in used_adapters: 
      results.append({'adapter': adapter, 'diff': diff})
  
  return sorted(results, key = lambda x: x['diff'])

def partI(input_data):
  current_jolts = 0
  used_adapters = []
  diffrences = []
  while len(used_adapters) < len(input_data):
    res = findNextAdapter(current_jolts, used_adapters, input_data)
    if len(res) == 0: break

    used_adapters.append(res[0]['adapter'])
    diffrences.append(res[0]['diff'])
    current_jolts = res[0]['adapter']

  return (diffrences.count(3) + 1) * diffrences.count(1)

def main():
  lines = open('in.txt').readlines()
  adapters = [int(line) for line in lines]
  print(partI(adapters))


if __name__ == "__main__":
  main()