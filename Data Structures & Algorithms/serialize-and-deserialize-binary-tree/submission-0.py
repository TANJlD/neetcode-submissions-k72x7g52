# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        string = []
        def travel(node):
            if not node:
                string.append("n")
                return
            string.append(str(node.val))
            travel(node.left)
            travel(node.right)
        travel(root)
        return " ".join(string)

    def deserialize(self, data):
        order = data.split(" ")
        indx = 0
        def makeTree():
            nonlocal indx
            if order[indx] == "n":
                indx += 1
                return None
            
            val = int(order[indx])
            root = TreeNode(val)
            indx += 1
            root.left = makeTree()
            root.right = makeTree()

            return root

        return makeTree()
        