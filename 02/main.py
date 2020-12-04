def partI(input_data):
  valid_count = 0
  for pass_data in input_data:
    letter_count = pass_data['password'].count(pass_data['letter'])
    if letter_count >= pass_data['min'] and letter_count <= pass_data['max']:
      valid_count += 1

  return valid_count

def partII(input_data):
  valid_count = 0
  for pass_data in input_data:
    password = pass_data['password']
    letter = pass_data['letter']
    minn = pass_data['min'] - 1
    maxx = pass_data['max'] - 1
    has_index_min = len(password) >= minn
    has_index_max = len(password) >= maxx
    
    if has_index_min and has_index_max:
      if (password[minn] == letter and password[maxx] != letter) or (password[maxx] == letter and password[minn] != letter):
        valid_count += 1
    
    if has_index_min and not has_index_max:
      if password[minn] == letter:
        valid_count += 1
  return valid_count

def main():
  lines = open('in.txt').readlines()
  data = []
  for line in lines:
    parts = line.split(':')
    data.append({
      'password': parts[1].strip(),
      'letter': parts[0].split(' ')[1][0],
      'min': int(parts[0].split(' ')[0].split('-')[0]),
      'max': int(parts[0].split(' ')[0].split('-')[1])
    })
  
  print(partI(data))
  print(partII(data))
    

if __name__ == "__main__":
  main()