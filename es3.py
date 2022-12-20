def maximum(t): 
    max_value = 0 
    for value in t:
        if value > max_value: 
            max_value = value 
    return max_value

def minimum(t):
  min_value = None
  for item in t:
    if min_value is None or item < min_value:
      min_value = item
  return min_value

def somma(t):
  sum = 0
  for i in t:
    sum += i
  return sum

def prod(t):
    product = 1
    for item in t:
        product *= item
    return product



def moda(t):
  mode = {}
  maxCount = 0
  for item in t:
    if item not in mode:
      mode[item] = 1
    else:
      mode[item] += 1
    maxCount = max(maxCount, mode[item])
  result = []
  for key, value in mode.items():
    if value == maxCount:
      result.append(key)
  # ritorna piu' mode  se ci sono
  #return result
  # ritorna una sola moda (come lo vuole lei)
  return result[0]

def avg(t):
    return sum(t) / len(t)

def median(t):
    t.sort()
    length = len(t)
    if length % 2 == 0:
        middle = length/2
        median = (t[middle] + t[middle-1])/2
    else:
        median = t[length // 2]
    return median