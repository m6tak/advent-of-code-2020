import re
def findBagByColor(color, ruleset):
  for bag in ruleset:
    if bag['color'] == color: return bag
  return None

def getBagContentColorCount(bag, color):
  for item in bag['color-counts']:
    if item['color'] == color: return item['count']
  return 0


def countBagsInside(bag, ruleset):  
  if 'no other' in bag['contents']: return 0

  count = 0
  for bag_color in bag['contents']:
    other_bag = findBagByColor(bag_color, ruleset)
    color_count = getBagContentColorCount(bag, bag_color)
    count += color_count + color_count * countBagsInside(other_bag, ruleset)
  
  return count 
    

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

def partII(input_data):
  gold_bag = findBagByColor('shiny gold', input_data)
  return countBagsInside(gold_bag, input_data)


def main():
  lines = open('in.txt').readlines()
  ruleset = []
  for line in lines:
    contents = line.split('contain')[1].replace('bags', '').replace('bag', '').replace('.', '').replace('\n', '').split(',')
    color_counts = []
    for color in contents:
      if 'no other' not in color:
        color_counts.append({'color': re.sub(r'[0-9]', '', color.strip()).strip(), 'count': int(re.findall(r'[0-9]', color)[0])})
    line_rules = {
      'color': line.split('contain')[0].replace('bags', '').strip(),
      'contents': [re.sub(r'[0-9]', '', color.strip()).strip() for color in contents],
      'color-counts': color_counts
    }
    ruleset.append(line_rules)
  
  
  print(partI(ruleset))
  print(partII(ruleset))



if __name__ == "__main__":
  main()