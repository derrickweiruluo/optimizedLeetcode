class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        maxLen = 0
        path = {}
        
        fileList = input.split("\n")
        for i in fileList:
            if "." not in i:  # while is a folder
                depth = i.count("\t")
                length = len(i.strip("\t"))
                path[depth] = length
                # print(depth, path[depth])
                # This is a step to update every file's length, when reach to the next file, the depth will be reset
                # "dir\n\tsubdir1111111111111111111111111111111111111\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
            else:
                depth = i.count("\t")
                curr = len(i) + sum([path[d] for d in range(depth)])
                maxLen = max(maxLen, curr)
                
        return maxLen
