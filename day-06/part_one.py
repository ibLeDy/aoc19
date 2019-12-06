with open("input.txt", "r") as f:
    data = f.read()
    print(data)

def search(root,key): 
    if root is None or root.val == key: 
        return root 

    if root.val < key: 
        return search(root.right, key) 
    
    return search(root.left, key) 


class Root:
def __init__(self, data):
    self.left = self.right = None
    self.val = data

class Solution:
    def insert(self,root,data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left,data)
                root.left = cur
            else:
                cur = self.insert(root.right,data)
                root.right = cur
        
        return root

tree = Solution()
root = None
for i in range(T):
    root = tree.insert(root, data)
