import random

def shuffle(values):
  for i in range(len(values)):
    j = random.randrange(len(values))
    values[i], values[j] = values[j], values[i]