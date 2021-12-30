'''
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.
'''


# Clarifications
# Garanteed: each node hasexactly two children nodes and is infinite
# just return the zig-zag label, NOT THE NODE.val

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        res = collections.deque()
        nodeCount = 1
        level = 1
        
        while label >= nodeCount * 2:
            nodeCount *= 2
            level += 1
        
        while label:
            res.appendleft(label)
            level_min = 2 ** (level - 1)
            level_max = 2 ** (level) - 1
            label = int((level_max + level_min - label)/2)
            level -= 1
        
        return res