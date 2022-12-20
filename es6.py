def print_handshakes(people):
  count = 0
  for i in range(len(people) - 1):
    for j in range(i + 1, len(people)):
      print(people[i] + " shakes hands with " + people[j])
      count += 1
  return count