class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        counter = collections.Counter()
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()     #split each cpdomain by space
            counter[domain] += int(count)        #add and count domain
            
            for i in range(len(domain)):
                if domain[i] == ".":            
                    counter[domain[i + 1:]] += int(count)     #add and count subdomains
                    
        
        return ["%d" " " "%s" %(counter[domain], domain) for domain in counter]
      
      
      
#   Your input
#   ["1000 mail.com","900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
#   Output
#   ["1901 mail.com","1951 com","900 google.mail.com","50 yahoo.com","1 intel.mail.com","5 wiki.org","5 org"]
#   Expected
#   ["1901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","1951 com"]
