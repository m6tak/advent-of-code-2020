def findMostRecentOccurence(haystack, needle):
  for i in reversed(range(len(haystack))):
    if haystack[i] == needle: return i
  return 0

def findMostRecentBetter(haystack, needle):
  return len(haystack) - 1 - haystack[::-1].index(needle)

def partI():
  turns = [9,12,1,4,17,0,18]
  for i in range(8,2021):
    last_spoken = turns[-1]
    if turns[:-1].count(last_spoken) >= 1:
      age = (i - 1) - (findMostRecentBetter(turns[:-1], last_spoken) + 1)
      turns.append(age)
    else:
      turns.append(0)
    
    #print(f'Turn {i}, spoken {turns[-1]}') 
  return turns[-1]
      



def main():
  print(partI())


if __name__ == "__main__":
  main()