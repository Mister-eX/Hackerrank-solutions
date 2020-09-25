""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree(root):
    if root is None:
        return True, None, None
    x, min_i, max_i= check_binary_search_tree(root.left)
    y, min_j, max_j= check_binary_search_tree(root.right)
    if x and y:
        if (root.left is None and root.right is None):
            return True, root.data, root.data
        elif (root.left is None) and (root.right is not None):
            if min_j > root.data:
                return True, root.data, min_j
        elif root.left and (not root.right):
            if max_i < root.data:
                return True, min_i, root.data
        elif root.left and root.right:
            if max_i < root.data and min_j >root.data:
                return True, min_i, max_j
    return False, None, None

def check_binary_search_tree_(root):
    res, _, _=check_binary_search_tree(root)
    return res
        
