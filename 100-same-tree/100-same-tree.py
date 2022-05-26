# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = [(p, q)]
        
        while (q != []):
            node1, node2 = q.pop(0)
            if node1 == None and node2 == None:
                continue
            elif node1 == None or node2 == None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                q.append((node1.left, node2.left))
                q.append((node1.right, node2.right))
        
        return True