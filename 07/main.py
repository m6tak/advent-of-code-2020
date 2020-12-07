import re
def findBagByColor(color, ruleset):
  for bag in ruleset:
    if bag['color'] == color: return bag

def bagSearch(bag, ruleset, default_bags):
  if not bag: return 0
  if bag['contents'] is 'no other': return 0
  if bag['color'] in default_bags: return 1

  for color in bag['contents']:
    if bagSearch(findBagByColor(color, ruleset), ruleset, default_bags): return 1

  return 0
    

  
  





def partI(input_data):
  bags = []
  for bag in input_data:
    if 'shiny gold' in bag['contents']: bags.append(bag['color'])

  
  count = 0
  for bag in input_data:
    count += bagSearch(bag, input_data, bags)

  return count

  

  

def main():
  numbers = '123456789'
  lines = open('in.txt').readlines()
  ruleset = []
  for line in lines:
    contents = line.split('contain')[1].replace('bags', '').replace('bag', '').replace('.', '').replace('\n', '').split(',')
    line_rules = {
      'color': line.split('contain')[0].replace('bags', '').strip(),
      'contents': [re.sub(r'[0-9]', '', color.strip()).strip() for color in contents]
    }
    ruleset.append(line_rules)
  
  #for bag in ruleset:
  #  print(bag)
  print(partI(ruleset))



if __name__ == "__main__":
  main()