def treefinder(slopex,slopey) -> int:
  with open('trees.txt', 'r') as f:
    trees = [x.strip() for x in f.readlines()]

  treecount = 0
  currentlocation = 0
  for counter, row in enumerate(trees):
    if counter % slopey == 0:
      if row[currentlocation % len(row)] == "#":
        treecount +=1
      currentlocation += slopex
  return(treecount)

if __name__ == "__main__":
  print(treefinder(1,1)*treefinder(3,1)*treefinder(5,1)*treefinder(7,1)*treefinder(1,2))
