# some methods create lists 
list = []
for x in range(8):
 list.append(2 ** x)
print('list is ', list)

list_1 = [2 ** x for x in range(8)]
print('list 1 is ', list_1)

list_2 = [x for x in range(12) if x % 2 == 0]
print('list 2 is ', list_2)

list_3 = [x+y for x in ['language ', 'program '] for y in ['python', 'C++']]
print('list 3 is ', list_3)
