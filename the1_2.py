line = input()
mylist = line.split()
summ = 0
for item in range(len(mylist), -1, -1):
  try:
    print(mylist[-1], end=' ')
    summ += int(mylist[-1])
    mylist.pop()
  except ValueError:
    print('current_root =', len(mylist))
    print('value = ', mylist[-1])
    break
print(summ)

