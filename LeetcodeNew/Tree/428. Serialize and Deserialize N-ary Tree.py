"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Serialize with preorder traversal where sentinel "#" indicates the final child of a node has been processed, so the function returns to its parent call.
# Deserialize by creating a deque (could also use an iterator with next() instead of popleft()).
# While the next item is not "#", create a child with the item, add the child to the list of children and recurse to create its subtree.
# Repeat until there are no more children, then ignore the "#".

class Codec:
    def serialize(self, root: 'Node') -> str:
        #Encodes a tree to a single string.
        
        serial = []
        
        def preorder(node):
            if not node:
                return None
            serial.append(str(node.val))
            for child in node.children:
                preorder(child)
            serial.append("#")
        preorder(root)
        return " ".join(serial)
        
	
    def deserialize(self, data: str) -> 'Node':
        #Decodes your encoded data to tree.

        if not data:
            return None
        tokens = deque(data.split())
        root = Node(int(tokens.popleft()), [])
        
        def treeBuilder(node):
            if not tokens:
                return
            while tokens[0] != "#":
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                treeBuilder(child)
            
            tokens.popleft()    # discard "#"
            
        treeBuilder(root)
        return root
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
