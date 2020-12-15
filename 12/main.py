def turn(direction, degrees, current_dir):
  dirs = ['N', 'W', 'S', 'E']
  dir_index = dirs.index(current_dir)
  rotations = int(degrees / 90)
  rot_dir = -1 if direction == 'R' else 1

  dir_index = (dir_index + (rot_dir * rotations)) % 4
  return dirs[dir_index]

def partII(input_data):
  facing = 'E'
  pos = {
    'N': 0,
    'S': 0,
    'W': 0,
    'E': 0
  }
  wp_pos = {
    'N': 1,
    'S': 0,
    'W': 0,
    'E': 10
  }

  for direction in input_data:
    if direction['dir'] == 'L' or direction['dir'] == 'R':
      facing = turn(direction['dir'], direction['value'], facing)
      continue
    
    if direction['dir'] == 'F':
      pos[facing] += direction['value']
      continue
  

def partI(input_data):
  facing = 'E'
  pos = {
    'N': 0,
    'S': 0,
    'W': 0,
    'E': 0
  }

  for direction in input_data:
    if direction['dir'] == 'L' or direction['dir'] == 'R':
      facing = turn(direction['dir'], direction['value'], facing)
      continue

    if direction['dir'] == 'F':
      pos[facing] += direction['value']
      continue
    
    pos[direction['dir']] += direction['value']
  
  return abs(pos['N'] - pos['S']) + abs(pos['E'] - pos['W'])

      


def main():
  lines = open('in.txt').readlines()
  directions = [{'dir': line[0], 'value': int(line[1:])} for line in lines]

  print(partI(directions))


if __name__ == "__main__":
  main()