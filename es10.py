import pandas as pd
import math
import collections

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

def costoMedioBiglietto():
   costo = 0
   for x in df['Fare'] :
       costo += x
   costo = costo/len(df['Fare'])
   return costo
   
def percentualeUomini():
    nUomini = 0
    for x in df['Sex']:
        if x == 'male':
            nUomini += 1
    return nUomini/len(df['Sex'])*100
    
def percentualeDonne():
    nDonne = 0
    for x in df['Sex']:
        if x == 'female':
            nDonne += 1
    return nDonne/len(df['Sex'])*100

def percentualeGenere():
    return 'M: ' + str(percentualeUomini()) + '\nF: ' + str(percentualeDonne())
    
def modaNome():
  mode = {}
  maxCount = 0
  list = df['Name']
  t = []
  for item in list:
      s = item[item.find('. ')+2:]
      s = s[:s.find(' ')]
      t.append(s)
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
  # ritorna una sola moda
  return result[0]
  
def distribuzioneEta():
  mode = {}
  t = df['Age']
  for item in t:
    if math.isnan(item):
       continue 
    if item not in mode:
      mode[item] = 1
    else:
      mode[item] += 1
  od = collections.OrderedDict(sorted(mode.items()))
  return od
    


