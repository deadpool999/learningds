
def printMultiple(x):
  for i in range(1, x  + 1):
    output = 3 * i;
    print(output)
    
printMultiple(5);

def printMultiples(x):
  list = []
  for i in range(1, x  + 1):
    output = 3 * i;
    list.append(output)
  return list
    
print(printMultiples(5));