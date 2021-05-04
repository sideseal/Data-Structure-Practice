# 연결 큐

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self, data):
        new_node = Node(data)
        self.front = new_node
        self.rear = new_node
        self.front.link = self.rear

    def __str__(self):
        print_queue = '[ '
        node = self.front
        while True:
            print_queue += str(node)
            if(node == self.rear):
                break
            try:
                node = node.link
            except:
                break
            print_queue += ', '
        print_queue += ' ]'
        return print_queue

    # 요소가 하나 들어있을 경우 삭제 불가하도록 설정
    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def enQueue(self, data):
        new_node = Node(data)
        self.rear.link = new_node
        self.rear = new_node

    def deQueue(self):
        if not self.isEmpty():
            node = self.front
            value = node.data
            self.front = self.front.link
            del node
            return value

    def peek(self):
        return self.front.data

if __name__=="__main__":
    m_queue = Queue(5)
    print(m_queue)
    m_queue.enQueue(7)
    print(m_queue)
    print('deQueue :', m_queue.deQueue())
    for i in range(10):
        m_queue.enQueue(i)
    print(m_queue)

# DEQUE

class Node:
    def __init__(self, data):
        self.data = data
        self.llink = None
        self.rlink = None
    
    def __str__(self):
        return str(self.data)

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        node = self.front
        print_deque = '[ '
        while True:
            print_deque += str(node)
            if node == self.rear:
                break
            try: node = node.rlink
            except: break
            print_deque += ', '
        print_deque += ' ]'
        return print_deque

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def insertFront(self, data):
        new_node = Node(data)
        if self.front == None and self.rear == None:
            self.front = new_node
            self.front.rlink = self.rear
            self.rear = new_node
            self.rear.llink = self.front
        else:
            self.front.llink = new_node
            new_node.rlink = self.front
            self.front = new_node

    def insertRear(self, data):
        new_node = Node(data)
        if self.rear == None and self.front == None:
            self.rear = new_node
            self.rear.llink = self.front
            self.front = new_node
            self.front.rlink = self.rear
        else:
            self.rear.rlink = new_node
            new_node.llink = self.rear
            self.rear = new_node

    def deleteFront(self):
        if self.isEmpty():
            return
        node = self.front
        value = node.data
        self.front = self.front.rlink
        del node
        return value

    def deleteRear(self):
        if self.isEmpty():
            return
        node = self.rear
        value.node.data
        self.rear = self.rear.llink
        del node
        return value

    def peekFront(self):
        return self.front.data
    
    def peekRear(self):
        return self.front.data
if __name__ == "__main__":
    m_deque = Deque()
    m_deque.insertFront(5)
    m_deque.insertFront(4)
    m_deque.insertFront(3)
    print(m_deque)
    m_deque.insertRear(10)
    m_deque.insertRear(9)
    print(m_deque)
    print('Delete Front :', m_deque.deleteFront())
    print(m_deque)
