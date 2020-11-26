#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, val):
        node = TreeNode(val)
        if self.root is None:
            self.root = node
            return
        else:
            queue = [self.root]
            while queue:
                cur_node = queue.pop(0)
                if cur_node.left is None:
                    cur_node.left = node
                    return
            # else:
            #     queue.append(cur_node.left)
                elif cur_node.right is None:
                    cur_node.right = node
                    return
                else:
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
            # else:
            #     queue.append(cur_node.right)


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.calculate_height(root) != -1

    def calculate_height(self, root):
        if not root:
            return 0
        left_h = self.calculate_height(root.left)
        right_h = self.calculate_height(root.right)
        if left_h == -1 or right_h == -1:  # 子树不平衡，提前结束（剪枝）
            return -1
        else:
            if abs(left_h - right_h) > 1:
                return -1
            else:
                return max(left_h, right_h) + 1  # 若平衡，则返回子树的深度


tree = Tree()
tree.add(3)
tree.add(9)
tree.add(20)
tree.add(None)
tree.add(None)
tree.add(15)
tree.add(7)

c = Solution()
res = c.isBalanced(tree.root)
print(res)
