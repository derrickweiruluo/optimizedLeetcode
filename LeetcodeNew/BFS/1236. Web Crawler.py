# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = set()
        visited.add(startUrl)

        queue = collections.deque([startUrl])
        target_domin = startUrl.split("//")[1].split("/")[0]
        
        while queue:
            curr_url = queue.popleft()
            for new_url in htmlParser.getUrls(curr_url):
                if new_url in visited:
                    continue
                if new_url.split("//")[1].split("/")[0] != target_domin:
                    continue
                queue.append(new_url)
                visited.add(new_url)
                
        return list(visited)
                
