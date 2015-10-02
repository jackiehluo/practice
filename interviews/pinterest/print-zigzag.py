def print_zigzag(root):
    cur_level, next_level = [root], []
    left_to_right = True
    while cur_level:
        cur = cur_level.pop()
        if cur:
            print cur.data + " "
            if left_to_right:
                next_level.append(cur.left)
                next_level.append(cur.right)
            else:
                next_level.append(cur.right)
                next_level.append(cur.left)
        if not cur_level:
            left_to_right = not left_to_right
            cur_level, next_level = next_level, cur_level