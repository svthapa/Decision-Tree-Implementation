import math
import numpy as np

THETA = 0.5


class Tree(object):

    def __init__(self, feature=None, ys=[], left=None, right=None):
        self.feature = feature
        self.ys = ys
        self.left = left
        self.right = right

    @property
    def size(self):
        size = 1
        if type(self.left) == int:
            size += 1
        else:
            size += self.left.size
        if type(self.right) == int:
            size += 1
        else:
            size += self.right.size
        return size

    @property
    def depth(self):
        left_depth = 1 if type(self.left) == int else self.left.depth
        right_depth = 1 if type(self.right) == int else self.right.depth
        return max(left_depth, right_depth)+1


def entropy(data):
    """Compute entropy of data.

    Args:
        data: A list of data points [(x_0, y_0), ..., (x_n, y_n)]

    Returns:
        entropy of data (float)
    """
    ### YOUR CODE HERE

    n_labels = len(data)
    count_label0 = np.count_nonzero([i[1] for i in data])
    count_label1 = n_labels - count_label0
    
    if n_labels != 0:
        prob1 = (count_label1 * 1.0 )/ n_labels
        prob0 = (count_label0 * 1.0) / n_labels
        
        if prob1 !=0:
            e_1 = -prob1 * math.log(prob1,2)
        else:
            e_1 = 0
        if prob0 != 0:
            e_0 = -prob0 * math.log(prob0,2)
        else:
            e_0 = 0
        entropy = e_1 + e_0
        
    else:
        entropy = 0
    
    return entropy
    
    ### END YOUR CODE

def gain(data, feature):
    """Compute the gain of data of splitting by feature.

    Args:
        data: A list of data points [(x_0, y_0), ..., (x_n, y_n)]
        feature: index of feature to split the data

    Returns:
        gain of splitting data by feature
    """
    ### YOUR CODE HERE

    # please call entropy to compute entropy
    Entropy_data = entropy(data)
    
    feature_data = list([i[0][:][feature], i[1]] for i in data)

    data_0 = list([i[0],i[1]] for i in feature_data if i[0] == 0)
    data_1 = list([i[0],i[1]] for i in feature_data if i[0] == 1)
 
    entropy_0 = entropy(data_0)
    entropy_1 = entropy(data_1)

    
    gain = Entropy_data - (entropy_0 * len(data_0)/len(data) + 
                           entropy_1 * len(data_1)/len(data))
    
    return gain
    ### END YOUR CODE
    
#d = [([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0), ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1)]
#f = 0
#print(len(d) - np.count_nonzero([i[1] for i in d]))
#print(gain(d, f))

def get_best_feature(data):
    """Find the best feature to split data.

    Args:
        data: A list of data points [(x_0, y_0), ..., (x_n, y_n)]

    Returns:
        index of feature to split data
    """
    ### YOUR CODE HERE

    # please call gain to compute gain
    max_gain_index = 0
    max_gain = 0.0
    for i in range(len(data[0][0])):
        gain_i = gain(data, i)
        if gain_i > max_gain:
            max_gain = gain_i
            max_gain_index = i
    
    return max_gain_index, max_gain
    ### END YOUR CODE

def build_tree(data):
    ys = {}
    for x, y in data:
        ys[y] = ys.get(y, 0) + 1
    if len(ys) == 1:
        return list(ys)[0]
    feature, gain = get_best_feature(data)
    ### YOUR CODE HERE

    # please split your data with feature and build two sub-trees
    # by calling build_tree recursively

    # left_tree = build_tree(...)
    # right_tree = build_tree(...)

    # Use THETA to split the continous feature
    
    t_l = list([i[0], i[1]] for i in data if i[0][feature] < THETA)
    t_r = list([i[0], i[1]] for i in data if i[0][feature] > THETA)
    
    if t_l == []:
        left_tree = max(ys, key = ys.get)
    else:
        left_tree = build_tree(t_l)
        
    if t_r == []:
        right_tree = max(ys, key = ys.get)
    else:
        right_tree = build_tree(t_r)
    
    ### END YOUR CODE
    return Tree(feature, ys, left_tree, right_tree)


def test_entry(tree, entry):
    x, y = entry
    if type(tree) == int:
        return tree, y
    if x[tree.feature] < THETA:
        return test_entry(tree.left, entry)
    else:
        return test_entry(tree.right, entry)


def test_data(tree, data):
    count = 0
    for d in data:
        y_hat, y = test_entry(tree, d)
        count += (y_hat == y)
    return round(count/float(len(data)), 4)


def prune_tree(tree, data):
    """Find the best feature to split data.

    Args:
        tree: a decision tree to prune
        data: A list of data points [(x_0, y_0), ..., (x_n, y_n)]

    Returns:
        a pruned tree
    """
    ### YOUR CODE HERE
    
    # please call test_data to obtain validation error
    # please call prune_tree recursively for pruning tree
    left = tree.left
    right = tree.right
    feature = tree.feature
    ys = tree.ys
    
    if not isinstance(left, Tree) and not isinstance(right, Tree):
        tree_new = max(ys, key = ys.get) 

        if (test_data(tree, data) <= test_data(tree_new, data)):
            tree = tree_new
        return tree
    
    else:
        
        data_left = list([i[0], i[1]] for i in data if i[0][feature] < THETA)
        data_right = list([i[0], i[1]] for i in data if i[0][feature] > THETA)
        
        if data_left == []:
        #if data == []:
            #left = max(ys, key = ys.get)
            left = left
        else:
            if isinstance(left, Tree):
                left = prune_tree(left, data_left)
        
        if data_right == []:
        #if data == []:
            #right = max(ys, key = ys.get)
            right = right
        else:
            if isinstance(right, Tree): 
                right = prune_tree(right, data_right)
            
        tree = Tree(feature, ys, left, right)
        
        tree_new = max(ys, key = ys.get) 
        if (test_data(tree, data) <= test_data(tree_new, data)):
            tree = tree_new
            
        return tree
        
        
    ### END YOUR CODE
