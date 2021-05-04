# 참고: https://blex.me/@baealex/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8A%B8%EB%A6%AC

# binary tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root = None

    # 전위순회
    def preorderTraversal(self, node):
        print(node, end="")
        if not node.left == None:
            self.preorderTraversal(node.left)
        if not node.right == None:
            self.preorderTraversal(node.right)

    # 중위순회
    def inorderTraversal(self, node):
        if not node.left == None:
            self.inorderTraversal(node.left)
        print(node, end="")
        if not node.right == None:
            self.inorderTraversal(node.right)

    # 후위순회
    def postorderTraversal(self, node):
        if not node.left == None:
            self.postorderTraversal(node.left)
        if not node.right == None:
            self.postorderTraversal(node.right)
        print(node, end="")

    def makeRoot(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node


if __name__ == "__main__":
    node = []
    node.append(Node("-"))
    node.append(Node("*"))
    node.append(Node("/"))
    node.append(Node("A"))
    node.append(Node("B"))
    node.append(Node("C"))
    node.append(Node("D"))

    m_tree = Tree()
    for i in range(int(len(node) / 2)):
        m_tree.makeRoot(node[i], node[i * 2 + 1], node[i * 2 + 2])

    print("이진 트리 전위 순회 : ", end="")
    m_tree.preorderTraversal(m_tree.root)
    print("\n" + "이진 트리 중위 순회 : ", end="")
    m_tree.inorderTraversal(m_tree.root)
    print("\n" + "이진 트리 후위 순회 : ", end="")
    m_tree.postorderTraversal(m_tree.root)

# thread binary tree

# 중위순회


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.is_thread_right = None

    def __str__(self):
        return str(self.data)


class ThreadTree:
    def __init__(self):
        self.root = None

    def inorderTraversal(self, node):
        while not node.left == None:
            node = node.left
        print(node, end="")
        while True:
            node = self.findThread(node)
            print(node, end="")
            if node.right == None:
                break

    def findThread(self, node):
        pre_node = node
        node = node.right
        if node == None:
            return node
        if pre_node.is_thread_right:
            return node
        while not node.left == None:
            node = node.left
        return node

    def makeRoot(self, node, left_node, right_node, thread):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node
        node.is_thread_right = thread


if __name__ == "__main__":
    node = []
    node.append(Node("-"))
    node.append(Node("*"))
    node.append(Node("/"))
    node.append(Node("A"))
    node.append(Node("B"))
    node.append(Node("C"))
    node.append(Node("D"))

    m_tree = ThreadTree()
    for i in range(int(len(node) / 2)):
        m_tree.makeRoot(node[i], node[i * 2 + 1], node[i * 2 + 2], False)

    m_tree.makeRoot(node[3], None, None, True)
    m_tree.makeRoot(node[4], None, None, True)
    m_tree.makeRoot(node[5], None, None, True)

    node[3].right = node[1]
    node[4].right = node[0]
    node[5].right = node[2]

    print("\n" + "스레드 이진 트리 중위 순회 : ", end="")
    m_tree.inorderTraversal(m_tree.root)

# binary search tree

import random


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data)


class SearchTree:
    def __init__(self):
        self.root = None

    def insertElement(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node

        node = self.root
        while True:
            pre_node = node
            if node.data > new_node.data:
                node = node.left
                if node == None:
                    node = new_node
                    pre_node.left = node
            elif node.data < new_node.data:
                node = node.right
                if node == None:
                    node = new_node
                    pre_node.right = node
            else:
                return
    
    def searchElement(self, data):
        node = self.root
        while True:
            if node.data > data:
                node = node.left
            elif node.data < data:
                node = node.right
            elif node.data == data:
                break
            else:
                return Node("탐색 결과 없음")
        return node
    
    def preorderTraversal(self, node):
        print(node, end=' ')
        if not node.left  == None : self.preorderTraversal(node.left)
        if not node.right == None : self.preorderTraversal(node.right)

    def inorderTraversal(self, node):
        if not node.left  == None : self.inorderTraversal(node.left)
        print(node, end=' ')
        if not node.right == None : self.inorderTraversal(node.right)
    
    def postorderTraversal(self, node):
        if not node.left  == None : self.postorderTraversal(node.left)
        if not node.right == None : self.postorderTraversal(node.right)
        print(node, end=' ')
    
if __name__ == "__main__":
    m_tree = SearchTree()

    m_tree.insertElement(250)
    for i in range(20):
        m_tree.insertElement(random.randint(0,500))

    print('\n' + '이진 탐색 트리 전위 순회 : ', end='') ; m_tree.preorderTraversal(m_tree.root)
    print('\n' + '이진 탐색 트리 중위 순회 : ', end='') ; m_tree.inorderTraversal(m_tree.root)
    print('\n' + '이진 탐색 트리 후위 순회 : ', end='') ; m_tree.postorderTraversal(m_tree.root)

    node = m_tree.searchElement(250)
    print('\n' + '탐색한 노드의 값 :', node)
    print(       '노드의 왼쪽 서브 트리 :', node.left)
    print(       '노드의 오른쪽 서브 트리 :', node.right)

    node = m_tree.searchElement(node.left.data)
    print('\n' + '탐색한 노드의 값 :', node)
    print(       '노드의 왼쪽 서브 트리 :', node.left)
    print(       '노드의 오른쪽 서브 트리 :', node.right)