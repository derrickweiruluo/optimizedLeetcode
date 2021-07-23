class Solution:
    def maxNumOfSubstrings(self, s):
        fst = {ch : i for i, ch in reversed(list(enumerate(s)))} #dict of 每个ch的first出现
        lst = {ch : i for i, ch in enumerate(s)}                 #dict of 每个ch的last出现
        
        ans, prev = [], -1
        for i in sorted(lst.values()): #sort这个dict的value， 然后loop
            ch_start, ch_end = fst[s[i]], lst[s[i]]  #start, end index of a ch
            right = ch_end
            while right >= ch_start and ch_start > prev and ch_end == i:
                ch_start = min(ch_start, fst[s[right]])
                ch_end   = max(ch_end, lst[s[right]])
                right -= 1
            if ch_start > prev and ch_end == i:
                ans.append(s[ch_start:ch_end + 1])
                prev = ch_end
        
        return ans
      
# 几个新写法，only amazon，超低频率，别死磕
