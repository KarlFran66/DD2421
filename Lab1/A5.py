import monkdata as m
import dtree as d
from drawtree_qt5 import drawTree


compareTree = d.buildTree(m.monk1, m.attributes, 2)
tree1 = d.buildTree(m.monk1, m.attributes)
tree2 = d.buildTree(m.monk2, m.attributes)
tree3 = d.buildTree(m.monk3, m.attributes)

checkTrain1 = d.check(tree1, m.monk1)
checkTrain2 = d.check(tree2, m.monk2)
checkTrain3 = d.check(tree3, m.monk3)

checkTest1 = d.check(tree1, m.monk1test)
checkTest2 = d.check(tree2, m.monk2test)
checkTest3 = d.check(tree3, m.monk3test)

print("Etrain:")
print('MONK-1:', 1-checkTrain1, 'MONK-2:', 1-checkTrain2, 'MONK-3:', 1-checkTrain3)

print("Etest:")
print('MONK-1:', 1-checkTest1, 'MONK-2:', 1-checkTest2, 'MONK-3:', 1-checkTest3)

drawTree(tree2)


# a5Is1 = d.select(m.monk1, m.attributes[4], 1)
# a5Is2 = d.select(m.monk1, m.attributes[4], 2)
# a5Is3 = d.select(m.monk1, m.attributes[4], 3)
# a5Is4 = d.select(m.monk1, m.attributes[4], 4)
#
# print('For the subset with a5 = 2')
# for i in range(6):
#     print('a%d:' % i, d.averageGain(a5Is2, m.attributes[i]))
# print(' ')
# print('For the subset with a5 = 4')
# for i in range(6):
#     print('a%d:' % i, d.averageGain(a5Is4, m.attributes[i]))
#
# print('For a5 = 1:')
# print(d.mostCommon(a5Is1))
# print()
# print('For a5 = 2:')
# print('a4 = 1:')
# print(d.mostCommon(d.select(a5Is2, m.attributes[3], 1)))
# print('a4 = 2:')
# print(d.mostCommon(d.select(a5Is2, m.attributes[3], 2)))
# print('a4 = 3:')
# print(d.mostCommon(d.select(a5Is2, m.attributes[3], 3)))
# print()
# print('For a5 = 3:')
# print('a6 = 1:')
# print(d.mostCommon(d.select(a5Is3, m.attributes[5], 1)))
# print('a6 = 2:')
# print(d.mostCommon(d.select(a5Is3, m.attributes[5], 2)))
#
# print()
# print('For a5 = 4:')
# print('a1 = 1:')
# print(d.mostCommon(d.select(a5Is4, m.attributes[0], 1)))
# print('a1 = 2:')
# print(d.mostCommon(d.select(a5Is4, m.attributes[0], 2)))
# print('a1 = 3:')
# print(d.mostCommon(d.select(a5Is4, m.attributes[0], 3)))
