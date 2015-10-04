def print_binary_tree(root):
    if not root: return
    current_level, next_level = [root], []
    while current_level:
        cur = current_level.pop(0)
        if cur:
            print str(cur.data) + " "
            next_level.append(cur.left)
            next_level.append(cur.right)
        if not current_level:
            current_level, next_level = next_level, current_level