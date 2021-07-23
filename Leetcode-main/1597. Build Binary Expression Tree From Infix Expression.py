# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Standard parser implementation based on this BNF
    #   s := expression
    #   expression := term | term { [+,-] term] }
    #   term := factor | factor { [*,/] factor] }
    #   factor :== digit | '(' expression ')'
    #   digit := [0..9]

class Solution(object):
    def expTree(self, s):
        tokens = collections.deque(list(s))
        return self.parse_expression(tokens)
    
    def parse_expression(self, tokens):
        lhs = self.parse_term(tokens)
        while len(tokens) > 0 and tokens[0] in ['+', '-']:
            op = tokens.popleft()
            rhs = self.parse_term(tokens)
            lhs = Node(val=op, left = lhs, right = rhs)
        return lhs
    
    def parse_term(self, tokens):
        lhs = self.parse_factor(tokens)
        while len(tokens) > 0 and tokens[0] in ['*', '/']:
            op = tokens.popleft()
            rhs = self.parse_factor(tokens)
            lhs = Node(val=op, left = lhs, right = rhs)
        return lhs
    
    def parse_factor (self, tokens):
        if tokens[0] == '(':
            tokens.popleft()
            node = self.parse_expression(tokens)
            tokens.popleft()
            return node
        else:
            token = tokens.popleft()
            return Node(val = token)
        
        
