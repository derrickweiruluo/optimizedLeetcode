class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        fileMap = collections.defaultdict(list)
        
        for path in paths:
            parseData = path.split()
            directory = parseData[0]
            for file in parseData[1:]:
                # fileName, char, content = file.partition("(")
                fileName, content = file.split("(")
                fileMap[content].append(directory + "/" + fileName)
        
        
        return [filePath for filePath in fileMap.values() if len(filePath) > 1 ]
