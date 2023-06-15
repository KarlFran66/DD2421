import dtree as d
import monkdata as m
import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

def completePruning(tree, valSet):
    allPrunedTrees = d.allPruned(tree)
    bestTree = tree
    existBestTree = False
    for oneTree in allPrunedTrees:
        if d.check(oneTree, valSet) >= d.check(bestTree, valSet):
            bestTree = oneTree
            existBestTree = True
    if existBestTree == False:
        return bestTree
    else:
        return completePruning(bestTree, valSet)


def main():
    monkTree = m.monk1
    monkVal = m.monk1test
    fraction = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    parameter_fraction = []
    classification_error = []
    for f in fraction:
        for i in range(100):
            monk1train, monk1val = partition(monkTree, f)
            monk1tree = d.buildTree(monk1train, m.attributes)
            best1tree = completePruning(monk1tree, monk1val)
            parameter_fraction.append(f)
            classification_error.append(1 - d.check(best1tree, monkVal))
    data = {'Fraction': parameter_fraction, 'Classification Error': classification_error}
    df = pd.DataFrame(data)
    print('Mean:')
    print(df.groupby(['Fraction']).mean())
    print('Std:')
    print(df.groupby(['Fraction']).std())
    # sns.violinplot(data=df, x='Fraction', y='Classification Error', inner='box', palette='Set2')
    sns.set(style='whitegrid')
    sns.lineplot(data=df, x='Fraction', y='Classification Error')
    plt.show()


if __name__ == '__main__':
    main()
