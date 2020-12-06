def getLowerHalf(minn, maxx):
  return (maxx - int((maxx - minn)/2) - 1) if maxx - minn > 1 else minn

def getUpperHalf(minn, maxx):
  return (minn + int((maxx - minn)/2) + 1) if maxx - minn > 1 else maxx

def getRow(bpass):
  minn = 0
  maxx = 127
  index = 0
  while maxx - minn > 0 and index < 7:
    if bpass[index] is 'F': maxx = getLowerHalf(minn, maxx)
    elif bpass[index] is 'B': minn = getUpperHalf(minn, maxx)

    index += 1
  
  return maxx

def getSeat(bpass):
  minn = 0
  maxx = 7
  index = 7
  while maxx - minn > 0 and index < len(bpass):
    if bpass[index] is 'L': maxx = getLowerHalf(minn, maxx)
    elif bpass[index] is 'R': minn = getUpperHalf(minn, maxx)

    index += 1
  
  return maxx

def parseBpass(bpass):
  row = getRow(bpass)
  seat = getSeat(bpass)
  sid = (row * 8) + seat
  return {'row': row, 'seat': seat, 'sid': sid}

def partI(input_data):
  sids = []
  for bpass in input_data:
    sids.append(parseBpass(bpass)['sid'])
  
  ssids = sorted(sids)
  return ssids[-1]

def partII(input_data):
  sids = []
  for bpass in input_data:
    sids.append(parseBpass(bpass)['sid'])
  
  ssids = sorted(sids)
  for i in range(1, len(ssids)):
    if ssids[i] - ssids[i - 1] > 1: return ssids[i] - 1

def main():
  data = open('in.txt').readlines()
  print(partI(data))
  print(partII(data))

  

if __name__ == "__main__":
  main()