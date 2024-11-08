class BSTNode:
    def __init__(self,key,data,left=None,right=None,parent=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __lt__(self,other):
        return self.key < other.key
    def __le__(self,other):
        return self.key <= other.key
    def __gt__(self,other):
        return self.key > other.key
    def __ge__(self,other):
        return self.key >= other.key
    

class BST:
    def __init__(self,root=None):
        self.root = root

    def _LocateParent_(self,key):
        parent = self.root.parent
        currNode = self.root
        while currNode:
            parent = currNode
            if key < currNode.key:
                currNode = currNode.left
            else:
                currNode = currNode.right
        return parent
            
    
    def _Transplate_(self,u, v):
        p = u.parent
        if not p:
            self.root = v
        elif u == p.left:
            p.left = v
        else:
            p.right = v
        if v:
            v.parent = p

    def Insert(self,key,data):
        parent = self._LocateParent_(key)
        newNode = BSTNode(key,data)
        newNode.parent = parent
        if parent:
            self.root = newNode
        elif newNode < parent:
            parent.left = newNode
        else:
            parent.right = newNode


    def Search(self,key):
        return self._FindNode_(key).data

    def _FindNode_(self,key):
        currNode = self.root
        while currNode and currNode.key != key:
            if key < currNode.key:
                currNode = currNode.left
            else:
                currNode = currNode.right
        return currNode

    def MinKey(self,node = None):
        if not node:
            node = self.root
        while traverse.left:
            traverse = traverse.left
        return traverse.key

    def MaxKey(self, node = None):
        if not node:
            node = self.root
        while traverse.right:
            traverse = traverse.right
        return traverse.key

    def RangeSearch(self,lower,upper):
        pass

    def Delete(self,key):
        z = self._FindNode_(key)
        if not z.left:
            self._Transplate_(z,z.right)
        elif not z.right:
            self._Transplate_(z,z.left)
        else:
            y = self.Successor(key)

    def Successor(self,key):
        pass

    def Predecessor(self,key):
        pass            

    def InorderWalk(node):
        if node:
            BST.InorderWalk(node.left)
            print(node.key)
            BST.InorderWalk(node.right)

    def PreorderWalk(node):
        if node:
            print(node.key)
            BST.PreorderWalk(node.left)
            BST.PreorderWalk(node.right)

    def PostorderWalk(node):
        if node:
            BST.PostorderWalk(node.left)
            BST.PostorderWalk(node.right)
            print(node.key)

    def _RightRotate_(self,node):
        pass

    def _LeftRotate_(self,node):
        pass