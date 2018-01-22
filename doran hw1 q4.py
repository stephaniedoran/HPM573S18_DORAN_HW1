yours = ['Yale', 'MIT', 'Berkeley']
mine = ['CWRU', 'OhioU', 'Emory']

ours1 = mine + yours
print('Ours1 is', ours1)

ours2 = []
ours2.append(mine)
ours2.append(yours)
print('Ours2 is', ours2)

print('Ours 1 is a list with six items, ours2 is a list with two items. '
      'Each item in ours2 is a list with three items')

yours[1]='OhioState'

print(ours1)
print(ours2)
print('Ours1 is its own list in itself. Ours2 is drawing on the each list as is it being made')
