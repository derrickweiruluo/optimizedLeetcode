# Design a data structure that simulates an in-memory file system.

# Implement the FileSystem class:

# FileSystem() Initializes the object of the system.

# List<String> ls(String path)
#     If path is a file path, returns a list that only contains this file's name.
#     If path is a directory path, returns the list of file and directory names in this directory.
#     The answer should in lexicographic order.

# void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. 
# If the middle directories in the path do not exist, you should create them as well.

# void addContentToFile(String filePath, String content)
#     If filePath does not exist, creates that file containing given content.
#     If filePath already exists, appends the given content to original content.
# String readContentFromFile(String filePath) Returns the content in the file at filePath.

class Node():
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = Node()

    # If filePath does not exist, creates that file containing given content.
    # If filePath already exists, appends the given content to original content.
    
    def find(self, path):
        curr = self.root
        if path == "/":
            return curr
        for word in path.split("/")[1:]:
            curr = curr.child[word]
        return curr
    
    def ls(self, path: str) -> List[str]:
        curr = self.find(path)
        if curr.content:
            return [path.split("/")[-1]]   # ask for a list file name
        return sorted(curr.child.keys())   # return a list of sub dir and file names

    def mkdir(self, path: str) -> None:
        self.find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.find(filePath)
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.find(filePath)
        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
