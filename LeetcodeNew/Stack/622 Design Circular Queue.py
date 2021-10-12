'''
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. 

*** But using the circular queue, we can use the space to store new values.

'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None] * k
        self.size = 0
        # 下两个最重要，是两个根据arr size变化而变化的pointers
        # 这个circular array不删除不pop，只是单单的利用pointer来覆盖当前值
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % len(self.arr)  # modulo of cur arr length
        self.arr[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.arr) # modulo of cur arr length
        # no action hear , just move the front pointer to the pos
        self.size -=1
        return True
        
    def Front(self) -> int:
        return self.arr[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.arr[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.arr)


