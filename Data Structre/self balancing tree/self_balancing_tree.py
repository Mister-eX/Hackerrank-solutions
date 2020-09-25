class Node:
    def __init__(self, val):
        self.val = val
        self.height= 0
        self.left= None
        self.right= None

def insert(root, val):
    if root is None:
        return Node(val)

    if val < root.val:
        root.left = insert(root.left, val)

    elif val > root.val:
        root.right = insert(root.right, val)

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance_factor = get_balancefactor(root)

    if balance_factor > 1 and val < root.left.val:
        return clockwise_rotation(root)

    if balance_factor < -1 and val > root.right.val:
        return anti_clockwise_rotation(root)

    if balance_factor > 1 and val > root.left.val:
        root.left = anti_clockwise_rotation(root.left)
        return clockwise_rotation(root)

    if balance_factor < -1 and val < root.right.val:
        root.right = clockwise_roation(root.right)
        return anti_clockwise_rotation(root)

    return root



def clockwise_roation(root):
    new_root = root.left
    temp = new_root.right

    new_root.right= root
    root.left = temp

    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    return new_root


def anti_clockwise_rotation(root):
    new_root = root.left
    temp = new_root.left

    new_root.left = root
    root.right = temp

    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    return new_root



def get_balancefactor(root):
    if root is None:
        return 0
    return get_height(root.left) - get_height(root.right)


def get_height(root):
    if root is None:
        return -1
    return root.height