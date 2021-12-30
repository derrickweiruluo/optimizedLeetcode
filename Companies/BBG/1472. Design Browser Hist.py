

class Node:
    
    def __init__(self, url, prev, next):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage, None, None)
        self.cur = self.head

    def visit(self, url: str) -> None:
        node = Node(url, None, None)
        self.cur.next, node.prev = node, self.cur
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        # Return the current url after moving back in history at most steps.
        while self.cur.prev and steps:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.url

    def forward(self, steps: int) -> str:
        # Return the current url after moving back in history at most steps.
        while self.cur.next and steps:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)