import copy
import random
from helper import read_data
from solution import test_data, build_tree, prune_tree
import numpy as np

def test_tree_accuracy(data):
    random.seed(1)
    print('='*58)
    trainlen = len(data[('train', 'vector')])

    train_data = list(zip(
        data[('train', 'vector')],
        data[('train', 'labels')]))
    random.shuffle(train_data)

    #print(np.count_nonzero([i[1] for i in train_data]))
    
    #fi = [[i[0][:][0], i[1]] for i in train_data]
    #print(len([[i[0],i[1]] for i in fi if i[0] == 0]))
    #print(len(fi))
    #print(train_data)
    
    tree = build_tree(train_data[:int(trainlen * 0.8)])

    Ptree = prune_tree(
        copy.deepcopy(tree), train_data[int(trainlen * 0.8):])
    
    print('Accuracy on train data without pruning ===========>', 
          test_data(tree, train_data[:int(trainlen * 0.8)]))
    print(
        'Validate accuracy on tree without pruning ========>',
        test_data(tree, train_data[int(trainlen * 0.8):]))
    
    print('Accuracy on train data with pruning ==============>', 
          test_data(Ptree, train_data[:int(trainlen * 0.8)]))
    
    print(
        'Validate accuracy on tree with pruning ===========>',
        test_data(Ptree, train_data[int(trainlen * 0.8):]))
    print(
        'Test accuracy on tree without pruning ============>',
        test_data(tree, list(zip(
            data[('test', 'vector')],
            data[('test', 'labels')]))))
    print(
        'Test accuracy on tree with pruning ===============>',
        test_data(Ptree, list(zip(
            data[('test', 'vector')],
            data[('test', 'labels')]))))
    print('Tree size without pruning ========================> %6d' % (
        tree.size))
    print('Tree size with pruning ===========================> %6d' % (
        Ptree.size))
    print('Tree depth without pruning =======================> %6d' % (
        tree.depth))
    print('Tree depth with pruning ==========================> %6d' % (
        Ptree.depth))
    print('='*58)


if __name__ == '__main__':
    data = read_data(dataloc='../data/')
    test_tree_accuracy(data)
