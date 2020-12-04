def traverse_forest(forest, slopex, slopey):
  px = 0
  py = 0
  fh = len(forest)
  fw = len(forest[0])
  trees_encountered = 0

  while py < fh:
    if forest[py][px] == '#': trees_encountered += 1
    px = (px + slopex) % fw
    py += slopey
  
  return trees_encountered

def partI(input_data):
  return traverse_forest(input_data, 3, 1)

def partII(input_data):
  return (traverse_forest(input_data, 3, 1) * 
  traverse_forest(input_data, 5, 1) * 
  traverse_forest(input_data, 7, 1) *
  traverse_forest(input_data, 1, 2) *
  traverse_forest(input_data, 1, 1))

def main():
  lines = open('in.txt').readlines()
  forest = []

  for line in lines:
    forest_row = []
    for char in line:
      if char is '.' or char is '#': forest_row.append(char)
    forest.append(forest_row)

  print(partI(forest))
  print(partII(forest))


if __name__ == "__main__":
  main()