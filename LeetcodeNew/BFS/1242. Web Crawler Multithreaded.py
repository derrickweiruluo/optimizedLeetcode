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

# Summary
# We implement a classic BFS but the entries in our queue are future objects instead of primitve values. 
# A pool of at most max_workers threads is used to execute getUrl calls asynchronously. 
# Calling result() on our futures blocks until the task is completed or rejected.


from concurrent import futures

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        host_name = lambda url: url.split('/')[2]  # split by '/', the 2nd item of the splited list is the host name
        visited = set()
        visited.add(startUrl)
        
        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                for url in tasks.popleft().result():
                    if url not in visited and host_name(startUrl) == host_name(url):
                        visited.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))
        
        return list(visited)
