def validateYear(yearStr, minn, maxx):
  try:
    year_n = int(yearStr)
    return len(yearStr) == 4 and year_n >= minn and year_n <= maxx
  except ValueError:
    return False

def validateEcl(ecl):
  ecls = ['amb', 'blu', 'grn', 'gry', 'hzl', 'oth', 'brn']
  return ecl in ecls

def validateHeight(heightStr):
  if heightStr[-2:] == 'in':
    height = int(heightStr.replace('in', ''))
    return height >= 59 and height <= 76
  elif heightStr[-2:] == 'cm':
    height = int(heightStr.replace('cm', ''))
    return height >= 150 and height <= 193
  else: return False

def validateHcl(hclStr):
  if hclStr[0] != '#': return False
  allowedChars = '1234567890abcdef'
  for char in hclStr[1:]:
    if char not in allowedChars: return False
  return True

def validatePid(pidStr):
  if len(pidStr) != 9: return False
  try:
    int(pidStr)
    return True
  except ValueError:
    return False


def partI(input_data):
  valid_passports = []
  for passport in input_data:
    if len(passport.keys()) < 7: continue

    if 'cid' not in passport or len(passport.keys()) == 8:
      valid_passports.append(passport)
  return {'passports': valid_passports, 'count': len(valid_passports)}

def partII(input_data):
  passports = partI(input_data)['passports']
  valid_count = 0
  for passport in passports:
    if (validatePid(passport['pid']) and 
    validateHcl(passport['hcl']) and
    validateEcl(passport['ecl']) and
    validateHeight(passport['hgt']) and
    validateYear(passport['byr'], 1920, 2002) and
    validateYear(passport['iyr'], 2010, 2020) and
    validateYear(passport['eyr'], 2020, 2030)): valid_count += 1 
  
  return valid_count
    
    

def main():
  lines = open('in.txt').readlines()
  passports = []
  current_passport = {}
  for line in lines:
    if not line or line == ' ' or line == '\n':
      passports.append(current_passport)
      current_passport = {}
    else:
      parts = line.replace('\n', '').split(' ')
      for part in parts:
        if not part: continue
        kv = part.split(':')
        current_passport[kv[0]] = kv[1]
  passports.append(current_passport)

  print(partI(passports)['count'])
  print(partII(passports))

if __name__ == "__main__":
  main()
