def printBoard(board):
  board_str = ''
  for row in board:
    row_str = ''
    for char in row:
      row_str += char
    row_str += '\n'
    board_str += row_str
  print(board_str)

def findFirstSeat(board, x, y, xdir, ydir):
  while x < len(board[0]) - 1 and y < len(board) - 1:
    x += xdir
    y += ydir
    if board[y][x] != '.': return board[y][x]
  
  return '.'

def partI(input_data):
  changes = 0
  iteration = 0
  first = True
  while first or changes > 0:
    first = False
    states = []
    changes = 0
    for y in range(len(input_data)):
      for x in range(len(input_data[y])):
        adjecent_empty = 0
        adjecent_taken = 0
        if input_data[y][x] == '.': continue

        adjecent_empty += int(input_data[y + 1][x - 1] == 'L') + int(input_data[y + 1][x] == 'L') + int(input_data[y+1][x+1] == 'L')
        adjecent_empty += int(input_data[y][x - 1] == 'L')                  +               int(input_data[y][x + 1] == 'L')
        adjecent_empty += int(input_data[y - 1][x - 1] == 'L') + int(input_data[y - 1][x] == 'L') + int(input_data[y-1][x+1] == 'L')

        adjecent_taken += int(input_data[y + 1][x - 1] == '#') + int(input_data[y + 1][x] == '#') + int(input_data[y+1][x+1] == '#')
        adjecent_taken += int(input_data[y][x - 1] == '#')                  +               int(input_data[y][x + 1] == '#')
        adjecent_taken += int(input_data[y - 1][x - 1] == '#') + int(input_data[y - 1][x] == '#') + int(input_data[y-1][x+1] == '#')

        states.append({'pos': f'{x}:{y}', 'adjecent_empty': adjecent_empty, 'adjecent_taken': adjecent_taken})


    for state in states:
      x = int(state['pos'].split(':')[0])
      y = int(state['pos'].split(':')[1])

      if input_data[y][x] == 'L' and state['adjecent_taken'] == 0:
        input_data[y][x] = '#'
        changes += 1
        continue

      if input_data[y][x] == '#' and state['adjecent_taken'] >= 4:
        input_data[y][x] = 'L'
        changes += 1
        continue

    #print(f'Iteration: {iteration} - {changes} changes')
    iteration += 1

  taken_count = 0
  for row in input_data:
    for seat in row:
      if seat == '#': taken_count += 1
  
  return taken_count

def main():
  lines = open('in.txt').readlines()
  input_data = []
  header = True
  for line in lines:
    line = line.replace('\n', '')
    if header:
      chars = ['.']
      for char in line:
        chars.append('.')
        header = False
      chars.append('.')
      input_data.append(chars)

    chars = ['.']
    for char in line:
      chars.append(char)
    chars.append('.')
    input_data.append(chars)

  chars = []
  for char in input_data[-1]:
    chars.append('.')
  input_data.append(chars)

  print(partI(input_data))




if __name__ == "__main__":
  main()