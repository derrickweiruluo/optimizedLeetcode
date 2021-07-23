class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join(f"{len(string)}|{string}" for string in strs)
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        strIdx = 0
        while strIdx < len(s):
            divIdx = s.find("|", strIdx)
            strIdx = divIdx + 1 + int(s[strIdx: divIdx])
            res.append(s[divIdx + 1: strIdx])
        
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
