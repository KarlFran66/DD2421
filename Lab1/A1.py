import monkdata as m
from dtree import entropy

entropyMONK1 = entropy(m.monk1)
entropyMONK2 = entropy(m.monk2)
entropyMONK3 = entropy(m.monk3)

print('Entropy of MONK-1:')
print(entropyMONK1)
print('Entropy of MONK-2:')
print(entropyMONK2)
print('Entropy of MONK-3:')
print(entropyMONK3)
