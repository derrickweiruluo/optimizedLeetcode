'''Implement a thread-safe bounded blocking queue that has the following methods:

BoundedBlockingQueue(int capacity) The constructor initializes the queue with a maximum capacity.
void enqueue(int element) Adds an element to the front of the queue. If the queue is full, the calling thread is blocked until the queue is no longer full.
int dequeue() Returns the element at the rear of the queue and removes it. If the queue is empty, the calling thread is blocked until the queue is no longer empty.
int size() Returns the number of elements currently in the queue.
Your implementation will be tested using multiple threads at the same time. Each thread will either be a producer thread that only makes calls to the enqueue method or a consumer thread that only makes calls to the dequeue method. The size method will be called after every test case.

Please do not use built-in implementations of bounded blocking queue as this will not be accepted in an interview.'''

'''
The idea is to use two semaphores, pushing and pulling, to maintain the invariants of the queue.
Initially, no thread can dequeue (self.pulling.acquire()) until a thread has enqueued (self.pulling.release()).
When capacity elements have been enqueued, self.pushing.acquire() will block the thread until a dequeue releases the semaphore again.
Additionally, use a Lock so only a single thread can modify the actual queue at once.

'''

import threading

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)              
        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
        self.pushing.acquire() # decrease count of UNUSED semaphores       
        self.queue.append(element)              
        self.pulling.release() # increase count of USED semaphores

    def dequeue(self) -> int:
        self.pulling.acquire() # decrease count of USED semaphores               
        res = self.queue.popleft()                
        self.pushing.release() # increase count of UNUSED semaphores
        return res

    def size(self) -> int:
        return len(self.queue)